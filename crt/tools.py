import os


def get_all_directories(path):
    files = os.listdir(path)
    return files


def get_file_nesting(nest, size_n):
    s_name = 0
    index = 0
    l_dir = []
    while index < len(nest):
        if nest[index] == '<':
            if nest[index+1] == '>':
                t_dir = ([], 1)
            else:
                t_dir = get_file_nesting(nest[index+1:], size_n)
            if type(t_dir) is tuple:
                list_dir, ind = t_dir
            else:
                list_dir = t_dir
                ind = size_n - index
            print("tyt1")
            l_dir.append({f"{nest[s_name:index].replace(':', '')}": list_dir})
            index = index+ind + 1
            s_name = index+ind + 1
        if index+1 >= len(nest):
            if (nest[s_name:index+1]):
                print("tyt")
                l_dir.append(nest[s_name:index+1].replace(':', ''))
                if index + 1 >= size_n:
                    return l_dir
                return (l_dir, index)
            return (l_dir)
        if nest[index] == ':':
            if nest[s_name:index]:
                print("tyt")
                l_dir.append(nest[s_name:index].replace(':', ''))
            s_name = index
        if nest[index] == '>':
            if nest[s_name:index]:
                print("tyt")
                l_dir.append(nest[s_name:index].replace(':', ''))
            return (l_dir, index+1)
        index += 1
    return l_dir


# n = "asd:a1:a2:a3<po:po1<a:a2>>"
# n = "pope:pop2<py1:py:py3>:asd1<asd2:asdf:asd3<q:2>:asd4>:asd5:asd52"

# print(get_file_nesting("pope:pop2<py1:py:py3>:asd1<asd2:asdf:asd3<q:2>:asd4>:asd5:asd52"))
# print(get_file_nesting(n, len(n)))
