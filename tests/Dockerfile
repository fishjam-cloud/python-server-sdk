ARG UV_VERSION=0.8
ARG PYTHON_VERSION=3.11
FROM ghcr.io/astral-sh/uv:$UV_VERSION AS uv-image

ARG PYTHON_VERSION
FROM python:$PYTHON_VERSION-slim AS builder

COPY --from=uv-image /uv /uvx /bin/

WORKDIR /app

COPY pyproject.toml .

COPY examples/transcription/pyproject.toml ./examples/transcription/
COPY examples/poet_chat/pyproject.toml ./examples/poet_chat/
COPY examples/selective_subscription/pyproject.toml ./examples/selective_subscription/

COPY uv.lock .

RUN uv sync --locked --no-install-project --all-extras

COPY . /app
