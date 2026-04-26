<p align="center"><img src="logo/crt_logo_deep_blue.png" /></p>
<h2><p align="center">A fast and convenient tool for creating files</p></h2>

---

**crt** is a powerful command-line tool designed for quick and easy file creation, as well as generating projects based on predefined templates. It helps you save time and boost productivity by eliminating the need to manually create files and organize structures.

---

## Features

- **File creation**: instantly create files using simple commands.
- **Folder creation**: easily create nested directory structures.
- **Template support**: use and create templates for common projects and file types.
- **Template management**: create, view, delete, and rename custom templates.
- **Flexibility**: easily customize templates to fit your needs.

---

## Commands

- **files**: create files, folders, and nested structures.
- **temps**: create a project using a template.

---

## Command Description

### File and Folder Creation

Accepts a string with file and folder names (wrap the string in quotes `""`). Use `:` to separate items, and `<>` to define folders.

```console
crt {file_name} {extension}
```

---

### Template Management

| Command                             | Description                                      |
| ----------------------------------- | ------------------------------------------------ |
| `crt -v`                            | View all available templates                     |
| `crt -t {name}`                     | Apply an existing template                       |
| `crt -t {name} -f`                  | Apply a template with content filling            |
| `crt -t {name} -p {path}`           | Specify target directory for template creation   |
| `crt -t {name} --append`            | Create a new template from the current directory |
| `crt -t {name} --remove`            | Delete an existing template                      |
| `crt -t {name} --rename {new_name}` | Rename a template                                |

---

### .gitignore Generation

| Command                 | Description                                |
| ----------------------- | ------------------------------------------ |
| `crt -t gitignore py`   | Create `.gitignore` for Python             |
| `crt -t gitignore js`   | Create `.gitignore` for JavaScript/Node.js |
| `crt -t gitignore java` | Create `.gitignore` for Java               |
| `crt -t gitignore c`    | Create `.gitignore` for C                  |
| `crt -t gitignore c++`  | Create `.gitignore` for C++                |
| `crt -t gitignore c#`   | Create `.gitignore` for C#                 |
| `crt -t gitignore go`   | Create `.gitignore` for Go                 |

---

## Installation

```console
pip install crtfiles

---> 100%
```

---

## Examples

### Templates

#### 1) View Available Templates

```console
crt -v

--->

Available templates:
 Default:
  • postgres (12 files)
  • fastapi (22 files)
  • react (71 files)
  • tg_bot (19 files)
  • tg_bot_full (96 files)
  • gitignore (py, js, java, c, c++, go, c#)
```

---

#### 2) Create a Custom Template

Navigate to your project directory and run:

```console
crt -t my_template -a -p my_project

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
├── test/
├── build/
├── README.md
└── .gitignore
```

---

#### 3) Apply Template with Content Filling

```console
crt -t fastapi -p my_app -f

--->

Template 'fastapi' applied successfully to: .\\my_app
```

---

#### 4) Apply Template Without Content (Structure Only)

```console
crt -t fastapi -p my_app

--->

Template 'fastapi' applied successfully to: .\\my_app
```

---

#### 5) Rename a Custom Template

```console
crt -t my_template -rn my_temp

--->

Template renamed: 'my_template' → 'my_temp'
```

---

#### 6) Delete a Custom Template

```console
crt -t my_template -rm

--->

Template 'my_template' removed successfully!
```

---

### Files

#### 1) Create Files

```console
crt main.py:test.py:requirements.txt

--->

your_folder/
│
├── main.py
├── test.py
└── requirements.txt
```

---

#### 2) Create Files with Extension

```console
crt main:test py

--->

your_folder/
│
├── main.py
└── test.py
```

---

#### 3) Create Folders

```console
crt "src<>:image<>:models<>"

--->

your_folder/
│
├── src/
├── image/
└── models/
```

---

#### 4) Create Nested Folders

```console
crt "src<models<>:assets<>>:lib<models<>>"

--->

your_folder/
│
├── src/
│   ├── models/
│   └── assets/
│
└── lib/
    └── models/
```

---

#### 5) Create Nested Files Inside Folders

```console
crt "app<base.py:control.py>:backends<database<models.py>:base.py>"

--->

your_folder/
│
├── app/
│   ├── base.py
│   └── control.py
│
└── backends/
    ├── database/
    │   └── models.py
    └── base.py
```

---

## .crtignore Configuration

To exclude files and folders from templates, create a `.crtignore` file in the project root.

### Example `.crtignore`

```crtignore
__pycache__
.venv
venv
.git
.env
*.log
*.tmp
.DS_Store
Thumbs.db
```

---

## Note

If you are using Windows CMD, wrap the input string in quotes `""` to avoid conflicts with folder creation symbols `<>`.

---

## Feedback

I’m always happy to hear your feedback and suggestions for improving **crt**.

- Email: feed619pro@gmail.com
