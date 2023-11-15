FROM python:3.11 as requirements-stage
WORKDIR /tmp
RUN pip3 install poetry

# Копируем файлы и устанавливаем зависимости
COPY pyproject.toml poetry.lock* /tmp/
RUN poetry export -f requirements.txt --output requirements.txt --without-hashes

FROM python:3.11

# Устанавливаем зависимости
WORKDIR /code
COPY --from=requirements-stage /tmp/requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# Копируем код приложения
COPY ./app /code/app
#
# Команда для запуска
CMD uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
