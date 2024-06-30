import os
import click
from crt.tools import get_all_directories


def crt_files(ext, t_str_names):
    all_directories = get_all_directories('.')
    for str_names in t_str_names:
        for file_name in str_names.split(":"):
            if f"{file_name}.{ext}" not in all_directories:
                os.system(f"type NUL > {file_name}.{ext}")
                print(f"create {file_name}.{ext}")
            else:
                print("file exists")


def crt_dirs(t_str_names):
    all_directories = get_all_directories('.')
    for str_names in t_str_names:
        for dir_name in str_names.split(":"):
            if dir_name not in all_directories:
                os.system(f"mkdir {dir_name}")
                print(f"create {dir_name}")
            else:
                print("dir exists")
