import os
import pkgutil
import json

from pathlib import Path
from typing import Optional, Dict

from crt.tools import decode_from_base64, encode_to_base64, get_all_files, get_crtignore, get_main_crtignore, is_binary, is_text_file, read_any_file


def get_user_data_dir() -> Path:
    """
    Returns the correct directory for user data following OS standards
    """
    app_name: str = "crtfiles"
    if os.name == "nt":  # Windows
        base_dir = Path.home() / "AppData" / "Local" / app_name
    elif os.name == "posix":  # Linux/Mac
        xdg_data_home = os.environ.get("XDG_DATA_HOME")
        if xdg_data_home:
            base_dir = Path(xdg_data_home) / app_name
        else:
            base_dir = Path.home() / ".local" / "share" / app_name
    else:
        base_dir = Path.home() / f".{app_name}"

    base_dir.mkdir(parents=True, exist_ok=True)
    return base_dir


def get_template(name: str, t_default: bool = True, t_custom: bool = True) -> Optional[Dict]:
    """
    Get template by name from user data or package defaults
    """
    try:
        if t_default:
            # Check package defaults
            data = pkgutil.get_data(__name__, "data/templates.json")
            if data:
                temp_file = json.loads(data.decode("utf-8"))
                if name in temp_file:
                    return temp_file[name]
        if t_custom:
            # Check user templates
            data_dir = get_user_data_dir()
            templates_path = data_dir / "templates.json"
            if templates_path.exists():
                with open(templates_path, "r", encoding="utf-8") as f:
                    templates_data = json.load(f)
                return templates_data.get(name)

        return None
    except (FileNotFoundError, json.JSONDecodeError):
        return None


def get_all_template_names() -> Optional[Dict]:
    """
    Get template by name from user data or package defaults
    """
    try:
        default_names = {}
        custom_names = {}
        # Check package defaults
        data = pkgutil.get_data(__name__, "data/templates.json")
        if data:
            temp_file = json.loads(data.decode("utf-8"))
            for name in temp_file:
                default_names[name] = len(temp_file[name]["files"])

        # Check user templates
        data_dir = get_user_data_dir()
        templates_path = data_dir / "templates.json"
        if templates_path.exists():
            with open(templates_path, "r", encoding="utf-8") as f:
                templates_data = json.load(f)
            for name in templates_data:
                custom_names[name] = len(templates_data[name]["files"])

        return {
            "default_names": default_names,
            "custom_names": custom_names,
        }
    except (FileNotFoundError, json.JSONDecodeError):
        return None


def append_template(template_name: str, files_data: dict) -> bool:
    """
    Append or create a new template with files data
    """
    data_dir = get_user_data_dir()
    templates_path = data_dir / "templates.json"

    if not templates_path.exists():
        with open(templates_path, "w", encoding="utf-8") as f:
            json.dump({}, f, indent=2, ensure_ascii=False)

    with open(templates_path, "r", encoding="utf-8") as f:
        templates_data = json.load(f)

    templates_data[template_name] = files_data

    with open(templates_path, "w", encoding="utf-8") as f:
        json.dump(templates_data, f, indent=2, ensure_ascii=False)

    return True


def delete_template(template_name: str) -> bool:
    """
    Delete a template by name
    """
    data_dir = get_user_data_dir()
    templates_path = data_dir / "templates.json"

    if not templates_path.exists():
        return False

    with open(templates_path, "r", encoding="utf-8") as f:
        templates_data = json.load(f)

    if template_name in templates_data:
        del templates_data[template_name]
        with open(templates_path, "w", encoding="utf-8") as f:
            json.dump(templates_data, f, indent=2, ensure_ascii=False)
        return True

    return False


def create_template(temp_name: str, path: str) -> bool:
    """
    Create a new template from files in the specified path
    """
    ignore_files = get_main_crtignore() + get_crtignore(path=path)
    template_data: list[Path] = get_all_files(exclude_names=ignore_files, path=path)
    if template_data:
        if append_template(template_name=temp_name, files_data=template_data):
            return True
        else:
            return False

    return False


def rename_template(template_name: str, new_name: str):
    data_dir = get_user_data_dir()
    templates_path = data_dir / "templates.json"
    try:
        with open(templates_path, "r", encoding="utf-8") as f:
            templates_data = json.load(f)
        if template_name in templates_data:
            templates_data[new_name] = templates_data.pop(template_name)
            with open(templates_path, "w", encoding="utf-8") as f:
                json.dump(templates_data, f, indent=2, ensure_ascii=False)
        return True
    except:
        return False


def make_template(base_dir: Path, template: dict, fill: bool) -> bool:
    """
    Apply template to the specified directory
    """
    try:
        
        for dir_path in template["folders"]:
            full_path = base_dir / dir_path
            full_path.parent.mkdir(parents=True, exist_ok=True)
            if Path(full_path).exists():
                continue
            os.system(f'mkdir "{full_path}"')
        for file_path, content_b64 in template["files"].items():
            full_path = base_dir / file_path
            full_path.parent.mkdir(parents=True, exist_ok=True)

            if fill:
                content_bytes = decode_from_base64(content_b64)

                if is_text_file(full_path, content_bytes):
                    try:
                        content_text = content_bytes.decode("utf-8")
                        full_path.write_text(content_text, encoding="utf-8")
                    except UnicodeDecodeError:
                        full_path.write_bytes(content_bytes)
                else:
                    full_path.write_bytes(content_bytes)
            else:
                full_path.touch()

        return True
    except Exception as e:
        return False
