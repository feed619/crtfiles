import os
from crt.tools import (
    get_all_directories,
    is_correct_request,
    get_file_nesting,
)


def create_files(t_str_names: dict, ext=None, name=None):
    if type(t_str_names) is dict:
        for key in t_str_names:
            if name:
                full_name = name + "\\" + key
                if not os.path.isdir(full_name):
                    os.system(f'mkdir "{full_name}"')
            else:
                full_name = key
                if not os.path.isdir(full_name):
                    os.system(f'mkdir "{full_name}"')
            for file in t_str_names[key]:
                if type(file) is str:
                    if full_name and file:
                        file_name = f"{full_name}\{file}.{ext}" if ext else f"{full_name}\{file}"
                    elif file:
                        file_name = f"{file}.{ext}" if ext else f"{file}"
                    else:
                        file_name = None
                    if file_name:
                        if not os.path.isfile(file_name):
                            os.system(f"type NUL > {file_name}")
                else:
                    create_files(t_str_names=file, ext=ext, name=full_name)
    else:
        for file in t_str_names:
            if name:
                if not os.path.isdir(name):
                    os.system(f'mkdir "{full_name}"')
                full_name = name + "\\"
            else:
                full_name = ""
            if type(file) is str:
                if full_name:
                    file_name = f"{full_name}\{file}.{ext}" if ext else f"{full_name}\{file}"
                else:
                    file_name = f"{file}.{ext}" if ext else f"{file}"
                if not os.path.isfile(file_name):
                    os.system(f"type NUL > {file_name}")
            else:
                create_files(file, ext, full_name)


def crt_files(ext: str, t_str_names):
    ans = is_correct_request(t_str_names)
    if ans == 1:
        l_dir = get_file_nesting(t_str_names, len(t_str_names))
        create_files(l_dir, ext)
    elif ans == ">" or ans == "<":
        print(f"missing sign '{ans}' (use crt --help)")
    else:
        print(f"{ans} (use crt --help)")


def crt_dirs(t_str_names):
    all_directories = get_all_directories(".")
    for str_names in t_str_names:
        for dir_name in str_names.split(":"):
            if dir_name not in all_directories:
                os.system(f'mkdir "{dir_name}"')
                
