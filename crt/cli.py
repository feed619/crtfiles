# cli.py
import click
from crt.option import crt_files, crt_dirs, crt_temp

TEMP = "temp"
DIR = "dir"


@click.command()
@click.argument('ext')
@click.option('-n',
              '--name',
              required=True,
              multiple=True,
              type=str,
              help='main:config:setup',)
def main(ext, name):
    """Put extension file and use '-n' or '--name' and write the names of the files that need to be created using ':'"""
    if (ext == TEMP):
        crt_temp(name)
    elif (ext == DIR):
        crt_dirs(name)
    else:
        crt_files(ext, name)


if __name__ == '__main__':
    main()
