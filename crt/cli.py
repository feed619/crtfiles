# cli.py
import click
from crt.option import crt_files, crt_dirs


@click.command()
@click.argument('ext')
@click.option('-N',
              '--name',
              required=True,
              multiple=True,
              type=str,
              help='main:config:setup',)
def main(ext, name):
    """Put extension file and use '--files' and write the names of the files that need to be created using ':'"""
    if (ext == "dir"):
        crt_dirs(name)
    else:
        crt_files(ext, name)


if __name__ == '__main__':
    main()
