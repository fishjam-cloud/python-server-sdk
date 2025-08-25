# Local development

The project is managed using [uv](https://docs.astral.sh/uv/). Make sure to have it installed first.

Then install the dependencies

```console
uv sync --all-packages
```

## Generating protobuf

To generate Python protobuf definitions run

```console
uv run ./compile_proto.sh
```

## Testing

You can test the SDK by running

```console
uv run ci_test
```

In local development you can use

```console
uv run local_test
```

## Format & Lint

You can format code by running

```console
uv run format
```

You can check linter by running

```console
uv run lint
```

## Documentation

Documentation is generated via openapi-python-client.

To update documentation you need to:

- Go to https://github.com/fishjam-cloud/fishjam/blob/main/openapi.yaml and open the raw file.
- Copy the URL.
- Run `uv run update_client <copied-url>`
