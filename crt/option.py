import os
import click
from crt.templates import get_templates
from crt.tools import get_all_directories
# crt file -n ds:asd<a1:a2:a3<p1:p2:p3>>:po4:po6


def file_nesting(nest):
    # print(nest)
    s_name = 0
    index = 0
    l_dir = []
    while index < len(nest):
        if nest[index] == '<':
            list_dir, ind = file_nesting(nest[index+1:])
            l_dir.append({f"{nest[s_name:index].replace(':', '')}": list_dir})
            index = index+ind + 1
            s_name = index+ind + 1
        if nest[index] == ':':
            if nest[s_name:index]:
                l_dir.append(nest[s_name:index].replace(':', ''))
            s_name = index
        if nest[index] == '>':
            if nest[s_name:index]:
                l_dir.append(nest[s_name:index].replace(':', ''))
            return (l_dir, index+1)
        if index+1 == len(nest):
            print("tyt")
            l_dir.append(nest[s_name:index+1].replace(':', ''))

        index += 1
    return l_dir


print(file_nesting("pope:pop2<py1:py:py3>:asd1<asd2:asdf:asd3<q:2>:asd4>:asd5:asd52"))


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


# crt_dict_directories("asd:dsdsd:wewq1:3252das:fgsa:po")
