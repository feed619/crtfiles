<!-- <h1><p align="center">crt</p></h1> -->
<p align="center"><img src="https://i.postimg.cc/qR92HXsv/crt_logo_blue.png" /></p>
<h2><p align="center">быстрый и удобный инструмент для создания файлов</p></h2>

---

crt — мощный инструмент командной строки, предназначенный для быстрого и лёгкого создания файлов, а также позволяющий создавать проекты на основе предопределённых шаблонов. Этот инструмент поможет вам сэкономить время и повысить продуктивность, избавив от необходимости вручную создавать файлы и организовывать содержимое.

---

## Возможности

- **Создание файлов**: мгновенное создание файлов с помощью простых команд.
- **Создание папок**: лёгкое создание вложенных структур папок.
- **Поддержка шаблонов**: использование и создание шаблонов для часто используемых проектов и типов файлов.
- **Управление шаблонами**: создание, просмотр, удаление и переименование пользовательских шаблонов.
- **Гибкость**: простая настройка шаблонов под ваши нужды.

---

## Функции:

- **files**: создание файлов, папок и вложений.
- **temps**: создание проекта с использованием шаблона.

---

## Описание команд:

### Создание файлов и папок:

Принимает строку с именами файлов и папок (оберните строку в кавычки '"'), для перечисления используйте знак ':', для создания папок используйте знаки '<>'.

`crt {имя_файла} {расширение}`

### Управление шаблонами:

| Команда                             | Описание                                                                              |
| ----------------------------------- | ------------------------------------------------------------------------------------- |
| `crt -v`                            | Просмотр всех доступных шаблонов                                                      |
| `crt -t {имя}`                      | Применить существующий шаблон                                                         |
| `crt -t {имя} -f`                   | Применить шаблон с заполнением содержимого                                            |
| `crt -t {имя} -p {путь}`            | Указать целевую директорию где будет создан шаблон                                    |
| `crt -t {имя} --append`             | Создать новый шаблон из текущей директории (путь шаблона можно указать параметром -p) |
| `crt -t {имя} --remove`             | Удалить существующий шаблон                                                           |
| `crt -t {имя} --rename {новое_имя}` | Переименовать шаблон                                                                  |

### Генерация .gitignore:

| Команда                 | Описание                                    |
| ----------------------- | ------------------------------------------- |
| `crt -t gitignore py`   | Создать `.gitignore` для Python             |
| `crt -t gitignore js`   | Создать `.gitignore` для JavaScript/Node.js |
| `crt -t gitignore java` | Создать `.gitignore` для Java               |
| `crt -t gitignore c`    | Создать `.gitignore` для C                  |
| `crt -t gitignore c++`  | Создать `.gitignore` для C++                |
| `crt -t gitignore c#`   | Создать `.gitignore` для C#                 |
| `crt -t gitignore go`   | Создать `.gitignore` для Go                 |

## Установка

```console
pip install crtfiles

---> 100%
```

## Примеры

### Шаблоны:

#### 1) Просмотр Доступных шаблонов

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

#### 2) Создание пользовательского шаблона:

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
├──  test/
├──  build/
├──  README.md
└──  .gitignore
```

#### 3) Применение шаблона с заполнением содержимого

```console
crt -t fastapi -p my_app -f

--->

Template 'fastapi' applied successfully to: .\my_app

```

#### 4) Применение шаблона без заполнения (только структура):

```console
crt -t fastapi -p my_app

--->

Template 'fastapi' applied successfully to: .\my_app

```

#### 5) Изменение названия пользовательского шаблона

```console
crt -t my_template -rn my_temp

--->

Template renamed: 'my_template' → 'my_temp'
```

#### 6) Удаление Пользовательского шаблона

```console
crt -t my_template -rm

--->

Template 'my_template' removed successfully!
```

### Файлы:

#### 1) Создание файла:

```console
crt main.py:test.py:requirements.txt
--->
your_folder/
│
├── main.py
├── test.py
└── requirements.txt
```

#### 2) Создание файла с указанием расширения:

```console
crt main:test py
--->
your_folder/
│
├── main.py
└── test.py
```

#### 3) Создание папки:

```console
crt "src<>:image<>:models<>"

--->
your_folder/
│
├── src/
├── image/
└── models/
```

#### 4) Создание вложенных папок:

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

#### 5) Создание вложений (файлов внутри папок):

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

## Настройка .crtignore

Для исключения файлов и папок из шаблонов создайте файл .crtignore в корне проекта:
gitignore

### Пример .crtignore

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

## Внимание

Если вы работаете в консоли cmd, запрос необходимо заключать в кавычки "" во избежание конфликтов с символами создания папок '<>'.

## Обратная связь:

Я всегда рад вашим отзывам и предложениям по улучшению crt. Пожалуйста, оставляйте свои комментарии.
Электронная почта

- [Email](mailto:feed619pro@gmail.com)
