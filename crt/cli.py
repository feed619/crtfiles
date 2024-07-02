# cli.py
import click
from crt.option import crt_files, crt_temp


@click.group(chain=True,)
def main():
    """
    file: \tTo create files use 'file' use '-n' or '--name' and list the names in quotes to list use the ':' sign to create folders use brackets after the name '<','>' in brackets you can specify files, after all names indicate file extensions if not specified in the names.
    Example: file -n "file_name1:file_name2:dir_name1<>:dir_name2<file_name>" py\n
    temp: \tTo create a project use 'temp' use '-n' or '--name' and specify the name of the template, by default there are the following templates: web-front, web-back, app, project, config.
    Example: crt temp -n app
    """
    pass


@main.command('temp')
@click.option('-n',
              '--name',
              required=True,
              type=str,
              help='crt temp -n app',)
def c_temp(name):
    crt_temp(name)


@main.command("file")
@click.argument('ext',
                required=False,)
@click.option('-n',
              '--name',
              required=True,
              multiple=False,
              type=str,
              help='file -n "f_name1:f_name2:dir_name1<>:dir_name2<f_name>" py',)
def c_files(ext, name):
    print(ext, name)
    crt_files(ext, name)


if __name__ == '__main__':
    main()
