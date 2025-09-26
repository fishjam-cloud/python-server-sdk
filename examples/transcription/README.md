# Transcription demo

This directory contains a demo app, which uses [Fishjam](https://fishjam.io) and [Gemini Live API](https://ai.google.dev/gemini-api/docs/live)
for real-time transcription of ongoing calls.

The application contains an HTTP server written in [FastAPI](https://fastapi.tiangolo.com/)
and uses [uv](https://docs.astral.sh/uv/) for dependency management.

## Running

> ![NOTE] All commands should be run from the parent directory of this README

Make sure to [install uv](https://docs.astral.sh/uv/getting-started/installation/) if you don't have it already.
Once you have `uv` installed, fetch the dependencies with

```bash
uv sync
```

To run the app, you will need 3 environment variables:

- `FISHJAM_ID`: Your Fishjam ID, which you can get on the [Fishjam website](https://fishjam.io/app)
- `FISHJAM_MANAGEMENT_TOKEN`: Your Fishjam management token, which you can get on the [Fishjam website](https://fishjam.io/app)
- `GEMINI_API_KEY`: An API key for the Gemini API. You can generate one on the [Gemini website](https://aistudio.google.com/app/apikey).

Once you have these variables, you can run the demo with

```bash
FISHJAM_ID=<your-fishjam-id> \
FISHJAM_MANAGEMENT_TOKEN=<your-management-token> \
GEMINI_API_KEY=<your-api-token> \
uv run fastapi dev
```

Now, you can create peer tokens by going to <http://localhost:8000>.
You can then use the [minimal-react](https://github.com/fishjam-cloud/web-client-sdk/tree/main/examples/react-client)
demo app to connect as these peers and see your transcriptions live in the console!
