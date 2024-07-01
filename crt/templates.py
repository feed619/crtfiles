import json
import pkg_resources


def get_templates(name: str):
    try:
        print(name)
        template_path = pkg_resources.resource_filename(
            __name__, 'data/templates.json')
        with open(template_path, 'r', encoding='utf-8') as json_file:
            temp_file: dict = json.load(json_file)
        if (name in temp_file.keys()):
            return temp_file.get(name)
        return None
    except FileNotFoundError:
        print("JSON file not found.")
        return None
    except json.JSONDecodeError:
        print("Error reading JSON file.")
        return None


# print(get_templates("project"))
# def get_templates(name: str):
#     try:
#         # Используем pkg_resources для доступа к файлу внутри пакета
#         template_path = pkg_resources.resource_filename(
#             __name__, 'data/templates.json')

#         # Открываем и загружаем файл JSON
#         with open(template_path, 'r', encoding='utf-8') as json_file:
#             temp_file: dict = json.load(json_file)

#         # Выводим все ключи в загруженном файле для отладки
#         print("Загруженные ключи:", temp_file.keys())

#         # Проверяем наличие ключа и возвращаем его значение
#         if name in temp_file:
#             return temp_file.get(name)
#         else:
#             print(f"Ключ '{name}' не найден в файле JSON.")
#             return None
#     except FileNotFoundError:
#         print("Файл JSON не найден.")
#         return None
#     except json.JSONDecodeError:
#         print("Ошибка при чтении JSON файла.")
#         return None


# # Пример вызова функции
# result = get_templates("app")
# print("Результат:", result)
