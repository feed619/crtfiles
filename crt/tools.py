import os
import json
import pkgutil
import base64

from pathlib import Path
from typing import List, Optional, Union


def encode_to_base64(data: Union[str, bytes]) -> str:
    """Кодирует строку или байты в base64"""
    if isinstance(data, str):
        data = data.encode("utf-8")
    return base64.b64encode(data).decode("ascii")


def decode_from_base64(encoded: str) -> bytes:
    """Декодирует base64 в байты"""
    return base64.b64decode(encoded.encode("ascii"))


def is_binary(path: str) -> bool:

    binary_extensions = {
        ".svg",
        ".png",
        ".jpg",
        ".jpeg",
        ".gif",
        ".bmp",
        ".ico",
        ".webp",
        ".exe",
        ".dll",
        ".so",
        ".dylib",
        ".zip",
        ".tar",
        ".gz",
        ".7z",
        ".rar",
        ".pdf",
        ".doc",
        ".docx",
        ".xls",
        ".xlsx",
        ".mp3",
        ".mp4",
        ".avi",
        ".mov",
        ".wav",
        ".pyc",
        ".pyo",
        ".pyd",
    }
    return path.suffix.lower() in binary_extensions


def is_text_file(file_path: Path, content_bytes: bytes = None) -> bool:
    """
    Определяет, является ли файл текстовым
    """
    # По расширению
    text_extensions = {
        ".txt",
        ".py",
        ".js",
        ".html",
        ".css",
        ".json",
        ".xml",
        ".md",
        ".yml",
        ".yaml",
        ".ini",
        ".cfg",
        ".conf",
        ".sh",
        ".bash",
        ".zsh",
        ".fish",
        ".ps1",
        ".bat",
        ".cmd",
        ".gitignore",
        ".crtignore",
        ".svg",  # SVG может быть текстовым
        ".ts",
        ".jsx",
        ".tsx",
        ".vue",
        ".svelte",
        ".scss",
        ".sass",
        ".less",
        ".rst",
        ".tex",
        ".latex",
        ".bib",
        ".csv",
        ".toml",
        ".lock",
    }

    if file_path.suffix.lower() in text_extensions:
        return True

    # Если есть содержимое, проверяем наличие нулевых байтов
    if content_bytes:
        # Если в первых 1024 байтах нет нулевых байтов - вероятно текст
        return b"\0" not in content_bytes[:1024]

    # По умолчанию считаем бинарным
    return False


# def encode_to_base64(text: str) -> str:
#     return str(base64.b64encode(text.encode("utf-8")).decode("ascii"))


def read_any_file(file_path: str) -> Optional[Union[str, bytes]]:
    path = Path(file_path)

    if not path.exists():
        return None

    if not path.is_file():
        return None

    if is_text_file(file_path=path):
        try:
            return path.read_text(encoding="utf-8")
        except Exception as e:
            return None
    else:
        return path.read_bytes()


def expand_user_path(user_path: str) -> Path:
    expanded = os.path.expanduser(user_path)

    if not os.path.isabs(expanded):
        expanded = os.path.join(os.getcwd(), expanded)

    return Path(expanded).resolve()


def get_user_cwd():
    """Где пользователь находится в момент вызова"""
    return os.getcwd()


def get_all_directories(path) -> list:
    files = os.listdir(path)
    return files


def get_all_files(path: str, exclude_names: List[str] = []) -> list[Path]:
    template_data = {"folders": [], "files": {}}

    base_path = Path(path)

    if not base_path.exists():
        return []

    for item in base_path.glob("**/*"):
        should_exclude = False
        if item.name in exclude_names:
            should_exclude = True

        if not should_exclude:
            for parent in item.parents:
                if parent.name in exclude_names:
                    should_exclude = True
                    break

        if not should_exclude:
            rel_path = item.relative_to(base_path)
            key = str(rel_path)
            if item.is_dir():
                template_data["folders"].append(key)
            else:
                full_path = f"{path}\\{key}"
                content = read_any_file(file_path=full_path)
                if content:
                    template_data["files"][key] = encode_to_base64(data=content)
    return template_data


def get_main_crtignore() -> Optional[List[str]]:
    data = pkgutil.get_data(__name__, "data/.crtignore")
    if data:
        lines = []
        for line in data.decode("utf-8").splitlines():
            line = line.strip()
            if line and not line.startswith("#"):
                line = line.replace("**", "__")
                if line.endswith("\\") or line.endswith("/"):
                    line = line[:-1]
                lines.append(line)
        return lines
    return []


def get_crtignore(path) -> Optional[List[str]]:
    crtignore_path = Path(path) / ".crtignore"
    if crtignore_path.exists():
        with open(crtignore_path, "r", encoding="utf-8") as file:
            lines = []
            for line in file:
                line = line.strip()
                if line and not line.startswith("#"):
                    line = line.replace("**", "__")
                    if line.endswith("\\") or line.endswith("/"):
                        line = line[:-1]
                    lines.append(line)
            return lines
    return []


def get_file_nesting(nest, size_n) -> list:
    s_name = 0
    index = 0
    l_dir = []

    while index < len(nest):
        if nest[index] == "<":
            if nest[index + 1] == ">":
                t_dir = ([], 1)
            else:
                t_dir = get_file_nesting(nest[index + 1 :], size_n)
            if type(t_dir) is tuple:
                list_dir, ind = t_dir
            else:
                list_dir = t_dir
                ind = size_n - index
            l_dir.append({f"{nest[s_name:index].replace(':', '')}": list_dir})
            index = index + ind + 1
            s_name = index + ind + 1
        if index + 1 == len(nest):
            if nest[s_name:index]:
                if nest[index] == ">":
                    l_dir.append(nest[s_name:index].replace(":", ""))
                else:
                    l_dir.append(nest[s_name : index + 1].replace(":", ""))
                if index + 1 >= size_n:
                    return l_dir
                return (l_dir, index)
            return l_dir
        if index + 1 > len(nest):
            if nest[s_name:index]:
                l_dir.append(nest[s_name:index].replace(":", ""))
                if index + 1 >= size_n:
                    return l_dir
                return (l_dir, index)
            return l_dir
        if nest[index] == ":":
            if nest[s_name:index]:
                l_dir.append(nest[s_name:index].replace(":", ""))
            s_name = index
        if nest[index] == ">":
            if nest[s_name:index]:
                l_dir.append(nest[s_name:index].replace(":", ""))
            return (l_dir, index + 1)
        index += 1
    return l_dir


def is_correct_request(s_name: str):

    incor_symbols = [
        '"',
        "|",
        "?",
        "*",
        ";",
        "'",
        " ",
    ]

    for sym in s_name:
        if sym in incor_symbols:
            return f"don't use signs {sym} in names"

    cont_l_b = s_name.count("<")
    cont_r_b = s_name.count(">")
    if cont_l_b == cont_r_b:
        return 1
    if cont_l_b < cont_r_b:
        return "<"
    if cont_l_b > cont_r_b:
        return ">"


def load_json_file(path: str) -> dict:
    with open(path, "r", encoding="utf-8") as json_file:
        temp_file: dict = json.load(json_file)


def save_file(path: str, data: str) -> None:
    with open(path, "w", encoding="utf-8") as file:
        file.write(data)
