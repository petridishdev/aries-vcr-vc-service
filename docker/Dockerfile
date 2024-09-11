FROM python:3.12

WORKDIR /app

RUN pip install --no-cache-dir --upgrade pip
RUN pip install poetry

COPY pyproject.toml poetry.lock ./

RUN poetry config virtualenvs.create false
RUN poetry install --no-root --only main

COPY ../ ./

CMD ["fastapi", "run", "main.py", "--port", "80", "--proxy-headers"]