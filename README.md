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
crt file -n "main.py:test.py:requirements.txt"

--->
your_folder/
│
├── main.py
├── test.py
└── requirements.txt
```

### 2) Сreating a file with the extension option:

```console
crt file -n "main:test" py

--->
your_folder/
│
├── main.py
└── test.py
```

### 3) Creating a folder:

```console
crt file -n "src<>:image<>:models<>"

--->
your_folder/
│
├── src/
├── image/
└── models/
```

### 4) Creating subfolders:

```console
crt file -n "src<models<>:assets<>>:lib<models<>>"

--->
your_folder/
│
├── src/
│   ├── models/
│   └── assets/
│
└──  lib/
    └── models/

```

### 5) Creating attachments:

```console
crt file -n "app<base.py:control.py>:backends<database<models.py>:base.py>"

--->
your_folder/
│
├── app/
│   ├── base.py
│   └── control.py
│
└──  backends/
    ├── database/
    │   └── models.py
    └── base.py

```

### 6) Сreating a project using a template:

```console
crt temp -n app

--->
your_folder/
│
├── lib/
│   ├── screens/
│   ├── widgets/
│   ├── models/
│   ├── services/
│   ├── utils/
│   ├── assets/
│   └── main.py
│
├──  test/
├──  build/
├──  README.md
└──  .gitignore

```

## Примечание

if you are working in the cmd console, then the request must be wrapped in quotes to avoid conflicts with the folder creation characters '<>'

## Setting up templates

Вы можете легко добавлять и редактировать шаблоны для создания файлов. Например, чтобы добавить новый шаблон:

## Feedback:

Я всегда рад услышать ваши отзывы и предложения по улучшению crt. Пожалуйста, оставляйте свои отзывы.
