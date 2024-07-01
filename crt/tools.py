import os


def get_all_directories(path):
    files = os.listdir(path)
    return files


def get_file_nesting(nest):
    s_name = 0
    index = 0
    l_dir = []
    while index < len(nest):
        if nest[index] == '<':
            list_dir, ind = get_file_nesting(nest[index+1:])
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
            l_dir.append(nest[s_name:index+1].replace(':', ''))
        index += 1
    return l_dir
