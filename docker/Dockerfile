FROM python:3.12

WORKDIR /app

ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

RUN pip install --no-cache-dir --upgrade pip
RUN pip install poetry

COPY ../ ./

RUN poetry install

CMD ["fastapi", "run", "main.py", "--port", "80", "--proxy-headers"]