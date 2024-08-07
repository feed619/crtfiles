<!-- <h1><p align="center">crt</p></h1> -->
<p align="center"><img src="https://i.postimg.cc/4yGPyFjn/crt-logo-dark-blue.png" /></p>
<h2><p align="center">fast and convenient tool for creating files</p></h2>

---

crt - a powerful command line tool designed to create files quickly and easily, and also allows you to create projects based on predefined templates. This tool will help you save time and increase productivity by eliminating the need to manually create files and organize content.

---

## Possibilities

- **File Creation**: Create files instantly with simple commands.
- **Folder Creation**: Easily create nested folder structures.
- **Template support**: Use and create templates for frequently used projects and file types.
- **Flexibility**: Easily customize templates to suit your needs.

---

## Сapabilities :

- **files**: can create files, folders and attachments.
- **temps**: can create a project using a template (templates are stored in the "templates.json" file).

---

## Description сapabilities:

- **files**:
  accepts a string of folder and file names(wrap the string with names in quotes '"'), for enumeration use the sign ':', to create folders use '<>' signs.
  ext (optional option) - after specifying the line with files, indicate the extension of all these files separated by a space

  [crt {file_name} {ext}]

- **temps**:
  -t,--temp - specify the name of the template, by default there are the following templates: "web-front", "web-back", "app", "project", "config" .

  [crt -t {temp_name}]

---

## Installation

```console
pip install crtfiles

---> 100%
```

---

## Example

### 1) Creating a file:

```console
crt main.py:test.py:requirements.txt

--->
your_folder/
│
├── main.py
├── test.py
└── requirements.txt
```

### 2) Сreating a file with the extension option:

```console
crt main:test py

--->
your_folder/
│
├── main.py
└── test.py
```

### 3) Creating a folder:

```console
crt "src<>:image<>:models<>"

--->
your_folder/
│
├── src/
├── image/
└── models/
```

### 4) Creating subfolders:

```console
crt "src<models<>:assets<>>:lib<models<>>"

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
crt "app<base.py:control.py>:backends<database<models.py>:base.py>"

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
crt -t app

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

---

## Attention

if you are working in the cmd console, then the request must be wrapped in quotes "" to avoid conflicts with the folder creation characters '<>'

---

## Setting up templates

You can easily add and edit templates. To do this, write on the command line:

```console
pip show crtfiles

--->
Location: ...\Lib\site-packages\
```

open the "crt" folder, then open the "data" folder and add or edit templates in the "templates.json" file to suit your needs (add templates strictly according to the examples from the file, if you make a mistake the result can be disastrous)

---

## Feedback:

I'm always glad to hear your feedback and suggestions for improving crt. Please leave your feedback.

- [Email](mailto:feed619pro@gmail.com)
