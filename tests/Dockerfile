ARG UV_VERSION=0.8
ARG PYTHON_VERSION=3.11
FROM ghcr.io/astral-sh/uv:$UV_VERSION AS uv-image

ARG PYTHON_VERSION
FROM python:$PYTHON_VERSION-slim AS builder

COPY --from=uv-image /uv /uvx /bin/

WORKDIR /app

COPY pyproject.toml .
COPY uv.lock .

RUN uv sync --locked --no-install-project

COPY . /app

RUN uv sync --locked
