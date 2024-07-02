# cli.py
import click
from crt.option import crt_files, crt_dirs, crt_temp

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


@main.command('dir')
@click.option('-n',
              '--name',
              required=True,
              multiple=True,
              type=str,
              help='dir -n/--name [dir_name]',)
def c_dirs(name):
    crt_dirs(name)


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


if __name__ == '__main__':
    main()
