ARG UV_VERSION=0.8
ARG PYTHON_VERSION=3.10
FROM ghcr.io/astral-sh/uv:$UV_VERSION AS uv-image

ARG PYTHON_VERSION
FROM python:$PYTHON_VERSION-slim AS builder

COPY --from=uv-image /uv /uvx /bin/

WORKDIR /app

RUN --mount=type=cache,target=/root/.cache/uv \
    --mount=type=bind,source=uv.lock,target=uv.lock \
    --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    uv sync --locked --no-install-project

COPY . /app/
RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --locked
