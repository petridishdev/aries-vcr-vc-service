FROM python:3.12-slim

# Create unprivileged user and group for service
RUN addgroup vcservice
RUN useradd -g vcservice vcservice

WORKDIR /app

# make user owner of app folder
RUN chown -R vcservice:vcservice /app

RUN pip install --no-cache-dir --upgrade pip
RUN pip install poetry

COPY pyproject.toml poetry.lock ./

RUN poetry config virtualenvs.create false
RUN poetry install --no-root --only main

COPY ../ ./

USER vcservice

CMD ["fastapi", "run", "main.py", "--port", "8080", "--proxy-headers"]