# FormInspector

Проект e.Сom Test - это веб-приложение для определения заполненных форм. Использует FastAPI, MongoDB и Docker для удобной разработки и развертывания.

## Установка и Запуск

1. Клонируйте репозиторий:

```bash
git clone https://github.com/mumorgir22/e.com_test.git
```
2. Перейдите в директорию проекта:
```bash
cd e.com_test/
```
3. Соберите и запустите контейнеры Docker:
```bash
docker compose build
```
```bash
docker compose up -d
```
4. Импортируйте тестовые данные в MongoDB:
```bash
mongoimport --db mongodb --collection collection --file test/collection.json --jsonArray
```
5. #### Веб-приложение будет доступно по адресу (http://127.0.0.1:8000)

   Добавление форм в бд (POST запрос) (http://127.0.0.1:8000/add_template/)
   
   Получение заполненных форм или списка полей с их типами (POST запрос) (http://127.0.0.1:8000/get_form/)
   
   К примеру http://127.0.0.1:8000/get_form/?f_name1=value1&f_name2=value2)

## Тестирование
Для добавления новых записей в базу данных используйте скрипт `add_template_script.py`. Вы можете определить необходимые формы, изменив словарь `form` в коде скрипта.
```python
# Пример словаря form
form = {
    "name": "New Feedback Form",    # Имя шаблона формы
    "full_name": "text",            # Поле 1: text
    "phone": "phone",               # Поле 2: phone
    "email": "email",               # Поле 3: email
    "message": "text",              # Поле 4: text
    "date": "date"                  # Поле 5: date
    # Добавьте или измените поля по вашему усмотрению
}
```
1. Отредактируйте скрипт add_template_script.py, изменив словарь form в соответствии с вашими требованиями.
2. Запустите скрипт для добавления формы в базу данных:
```bash
python add_template_script.py
```

Для получения имени подходящего шаблона формы или при отсутствии такой формы - списка полей с типами, используйте скрипт `test_script.py`. Скрипт будет использовать список `data_list` из файла `params.py` для генерации случайных параметров запроса. Вы можете изменить содержимое списка `data_list` для ваших собственных тестов.
1. Отредактируйте файл `params.py`, изменив список `data_list` в соответствии с вашими требованиями.
2. Запустите скрипт для получения имени подходящего шаблона формы:
```bash
python test_script.py
```
Примеры вывода скрипта после выполнения теста:
```python
# Если найдены подходящая форма или формы
"New Survey Form"
"Survey Form"

# При отсутствии форм
{
    "email": "email",
    "phone": "phone",
    "user_name": "text",
    "birthdate": "date",
    "car": "text"
}
```
