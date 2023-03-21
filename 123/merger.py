import os
import sys


def counter():
    directory = os.scandir(os.getcwd())
    txt_files_list = []
    for file in directory:
        if 'txt' in file.name:
            lines_count = 0
            with open(file, encoding='utf-8') as f:
                for _ in f:
                    lines_count += 1
            txt_files_list.append((lines_count, file.name))
    return sorted(txt_files_list)


def merger():
    pattern = counter()
    path = os.path.join(os.getcwd(), 'merged.mrg')
    with open(path, 'w+', encoding='utf-8') as f:
        for i in pattern:
            file = open(f'{i[1]}', encoding='utf-8')
            content = file.read()
            file.close()
            f.write(f'{i[1]}\n{str(i[0])}\n{content}\n')


if __name__ == '__main__':
    merger()
    sys.exit()
