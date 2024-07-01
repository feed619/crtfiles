import os
import click
from crt.templates import get_templates
from crt.tools import get_all_directories


def crt_files(ext, t_str_names):
    all_directories = get_all_directories('.')
    for str_names in t_str_names:
        for file_name in str_names.split(":"):
            if f"{file_name}.{ext}" not in all_directories:
                if ext is '.':
                    os.system(f"type NUL > {ext}{file_name}")
                    print(f"create {ext}{file_name}")
                else:
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


def crt_temp(temp_name):
    d_temp = get_templates(temp_name)
    print(d_temp)
    if d_temp:
        for dir in d_temp:
            print(dir)
            for file in dir:
                print("\t", file)
