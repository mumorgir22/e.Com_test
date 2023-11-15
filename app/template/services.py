from starlette.datastructures import QueryParams

from app.core.determine_utils import determine_data_type
from app.core.mongo_db import collection


def template_service(payload: dict):  # Добавление форм в бд
    collection.insert_one({**payload})


def get_service(params: QueryParams) -> list | dict:
    list_of_name = []
    data = validate(dict(params))
    all_documents = collection.find({})
    for document in all_documents:
        copied_dict = {
            key: value for key, value in document.items() if key not in ("_id", "name")
        }
        if all(item in data.items() for item in copied_dict.items()):
            list_of_name.append(document["name"])
    return list_of_name if list_of_name else data


def validate(data: dict) -> dict:  # Создание словаря с типами полей
    new_data = {}
    for key, value in data.items():
        data_type = determine_data_type(value)
        new_data[key] = data_type
    return new_data
