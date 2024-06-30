import os


def crt_files(ext, n_str):
    for file_name in n_str.split(":"):
        print(f"create {file_name}.{ext}")
        os.system(f"echo > {file_name}.{ext}")


def crt_dirs(n_str):
    for dir_name in n_str.split(":"):
        print(f"create {dir_name}")
        os.system(f"mkdir {dir_name}")
