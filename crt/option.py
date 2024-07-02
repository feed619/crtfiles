import os
from crt.templates import get_templates
from crt.tools import get_all_directories, get_file_nesting


def c_f(t_str_names,  ext=None, name=None):
    if type(t_str_names) is dict:
        for key in t_str_names:
            if (name):
                full_name = name+"\\"+key
                print("tyt1")
                if not os.path.isdir(full_name):
                    os.system(f"mkdir {full_name}")
                    print("Создал папку ", full_name)
            else:
                full_name = key
                print("tyt2")
                if not os.path.isdir(full_name):
                    os.system(f"mkdir {full_name}")
                    print("Создал папку ", full_name)
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
                            print("Создал файл ", file_name)
                else:
                    c_f(file, full_name, ext)
    else:
        for file in t_str_names:
            print(file)
            if (name):
                print("tyt4")
                if not os.path.isdir(name):
                    os.system(f"mkdir {full_name}")
                    print("Создал папку ", name)
                full_name = name+'\\'
            else:
                full_name = ""
            if type(file) is str:
                if (full_name):
                    file_name = f"{full_name}\{file}.{ext}" if ext else f"{full_name}\{file}"
                else:
                    file_name = f"{file}.{ext}" if ext else f"{file}"
                print("tyt5")
                if not os.path.isfile(file_name):
                    os.system(f"type NUL > {file_name}")
                    print(f"создал файл {file_name}")
            else:
                c_f(file, ext, full_name)


def c_d(l_str_names):
    print(l_str_names)
    if type(l_str_names) is dict:
        for key in l_str_names.keys():
            l_str_names[key] = c_d(l_str_names[key])
    else:
        for index in range(len(l_str_names)):
            if type(l_str_names[index]) is dict:
                l_str_names[index] = c_d(l_str_names[index])
            else:
                if not '.' in l_str_names[index]:
                    l_str_names[index] = {l_str_names[index]: []}
    return l_str_names


def crt_files2(ext, t_str_names):
    l_dir = get_file_nesting(t_str_names, len(t_str_names))
    print(l_dir)
    c_f(l_dir, ext)


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
    l_temp = get_templates(temp_name)
    l_dir = c_d(l_temp)
    c_f(l_dir)


crt_temp("app")
# crt_files2(
#     "py", "pope:pop2<py1:py:py3<asd:dwd<qwew:ewe>>>:asd1<asd2:asdf:asd3<q:2>:asd4>:asd5:asd52")

# crt_files2(
#     "py", "asd<a1:a2<g2>:a3<po:po1>>:piop:ieqw<po<main>>")
# print(crt_files2("py", "pope"))
