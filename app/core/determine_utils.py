import re
from datetime import datetime


def determine_data_type(value) -> str:  # Валидация полей
    try:
        datetime.strptime(value, "%d.%m.%Y")
        return "date"
    except ValueError:
        try:
            datetime.strptime(value, "%Y-%m-%d")
            return "date"
        except ValueError:
            pass

    phone_pattern = re.compile(r"^(\s*)?(\+)?([- _():=+]?\d[- _():=+]?){10,14}(\s*)?$")
    if phone_pattern.match(value):
        return "phone"

    email_pattern = re.compile(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$")
    if email_pattern.match(value):
        return "email"

    return "text"
