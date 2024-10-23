FROM python:3.12-slim

WORKDIR /app

ARG uid=1001
ARG user=vcservice

# Add vcservice user
RUN useradd -U -ms /bin/bash -u $uid $user

# - In order to drop the root user, we have to make some directories writable
#   to the root group as OpenShift default security model is to run the container
#   under random UID.
RUN usermod -a -G 0 $user

# The root group needs access the directories under /app for the container to function in OpenShift.
RUN chown -R $user:root /app && \
    chmod -R ug+rw /app

RUN pip install --no-cache-dir --upgrade pip
RUN pip install poetry

COPY pyproject.toml poetry.lock ./

RUN poetry config virtualenvs.create false
RUN poetry install --no-root --only main

COPY ../ ./

USER $user

CMD ["fastapi", "run", "main.py", "--port", "8080", "--proxy-headers"]