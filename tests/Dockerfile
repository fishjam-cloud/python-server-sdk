ARG PYTHON_VERSION=3.10

FROM python:$PYTHON_VERSION-slim as builder

ARG POETRY_VERSION=2.1

ENV POETRY_HOME=/opt/poetry
ENV POETRY_VIRTUALENVS_IN_PROJECT=1
ENV POETRY_VIRTUALENVS_CREATE=1
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV POETRY_CACHE_DIR=/opt/.cache

RUN pip install "poetry==${POETRY_VERSION}"

WORKDIR /app

COPY pyproject.toml poetry.lock /app/
RUN poetry install --with=dev --no-root && rm -rf $POETRY_CACHE_DIR
COPY . /app/
