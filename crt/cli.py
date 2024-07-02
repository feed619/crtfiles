# cli.py
import click
from crt.option import crt_files, crt_files2, crt_dirs, crt_temp

TEMP = "temp"
DIR = "dir"


@click.group(chain=True)
def main():
    pass


@main.command('temp')
@click.option('-n',
              '--name',
              required=True,
              type=str,
              help='temp -n/--name app',)
def c_temp(name):
    crt_temp(name)
    # print("create temp", name)


@main.command('dir')
@click.option('-n',
              '--name',
              required=True,
              multiple=True,
              type=str,
              help='dir -n/--name [dir_name]',)
def c_dirs(name):
    crt_dirs(name)
    # print("create dir", name)


@main.command("file")
@click.argument('ext',
                required=False,)
@click.option('-n',
              '--name',
              required=True,
              multiple=False,
              type=str,
              help='-n/--name [file_name:file_name:...] ext',)
def c_files(ext, name):
    print(ext, name)
    crt_files2(ext, name)
    # crt_files(ext, name)
    # print("create file", name, ext)


# @click.command()
# @click.argument('ext')
# @click.option('-n',
#               '--name',
#               required=True,
#               multiple=True,
#               type=str,
#               help='main:config:setup',)
# def main(ext, name):
#     print(name)
#     """Put extension file and use '-n' or '--name' and write the names of the files that need to be created using ':'"""
#     if (ext == TEMP):
#         crt_temp(name)
#     elif (ext == DIR):
#         crt_dirs(name)
#     else:
#         crt_files(ext, name)
if __name__ == '__main__':
    main()
