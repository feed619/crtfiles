<p align="center">
<img src="docs/crt_logo_dark_blue.png" />
</p>

<h2>
    <p align="center">
        Fast and convenient tool for creating files
    </p>
</h2>

---

crt - a powerful command line tool designed to create files quickly and easily, and also allows you to create projects based on predefined templates. This tool will help you save time and increase productivity by eliminating the need to manually create files and organize content.

---

## Possibilities

- **Fast File Creation**: Create files instantly with simple commands.
- **Folder Creation**: Easily create nested folder structures.
- **Template support**: Use and create templates for frequently used projects and file types.
- **Flexibility**: Easily customize templates to suit your needs.

---

## Commands:

- **file**: use to create files, folders and attachments.
- **temp**: use to create a project using a template (templates are stored in the templates.json file).

## Command Options:

- **file**:
  -n,--name (required option) - accepts a string of folder and file names(wrap the string with names in quotes '"'), for enumeration use the sign ':', to create folders use '<>' signs.
  ext (optional option) - after specifying the line with files, indicate the extension of all these files separated by a space

- **temp**: -n,--name (required option) - specify the name of the template, by default there are the following templates: "web-front", "web-back", "app", "project", "config" .

---

## Installation

<div class="termy">

```console
pip install crtfiles

---> 100%
```

</div>

---

## Example

### 1) Creating a file:

```console
crt file -n "main.py:test.py:.gitignore"

--->
your_folder/
│
├── main.py
├── test.p
└── .gitignore
```

### 2) Creating a file:

```console
$ pip install fastapi

---> 100%
```

### 3) Creating a folder:

```console
$ pip install fastapi

---> 100%
```

### 4) Creating subfolders:

```console
$ pip install fastapi

---> 100%
```

### 5) Creating attachments:

```console
$ pip install fastapi

---> 100%
```

Этот пример сначала добавляет новый HTML-шаблон, а затем создает файл index.html с динамическим содержимым.

## Примечание

...

## Настройка шаблонов

Вы можете легко добавлять и редактировать шаблоны для создания файлов. Например, чтобы добавить новый шаблон:

## Обратная связь:

Я всегда рады услышать ваши отзывы и предложения по улучшению crt . Пожалуйста, отправляйте свои отзывы на наш GitHub репозиторий здесь.

```

```
