import os
from crt.templates import get_templates
from crt.tools import get_all_directories, get_file_nesting


def c_f(t_str_names, name):
    if type(t_str_names) is dict:
        for key in t_str_names:
            for file in t_str_names[key]:
                if (name):
                    full_name = name+"/"+key
                    if not os.path.isdir(full_name):
                        os.system(f"mkdir {full_name}")
                        print("Создал папку ", full_name)
                else:
                    full_name = key
                    if not os.path.isdir(full_name):
                        os.system(f"mkdir {full_name}")
                        print("Создал папку ", full_name)
                if type(file) is str:
                    # print(f"{full_name}/{file}")
                    pass
                else:
                    c_f(file, full_name)
    else:
        for file in t_str_names:
            if (name):
                if not os.path.isdir(name):
                    os.system(f"mkdir {name}")
                    print("Создал папку ", name)
                full_name = name+'/'
            else:
                full_name = ""
            if type(file) is str:
                # print(f"{full_name}{file}")
                pass
            else:
                c_f(file, full_name)


def crt_files2(ext, t_str_names):
    l_dir = get_file_nesting(t_str_names)
    c_f(l_dir, "")


def crt_files(ext, t_str_names):
    all_directories = get_all_directories('.')
    for str_names in t_str_names:
        for file_name in str_names.split(":"):
            if f"{file_name}.{ext}" not in all_directories:
                if ext == '.':
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
            for file in d_temp.get(dir):
                print("\t", file)


# crt_files2(
#     "py", "pope:pop2<py1:py:py3<asd:dwd<qwew:ewe>>>:asd1<asd2:asdf:asd3<q:2>:asd4>:asd5:asd52")
