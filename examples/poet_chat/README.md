# Limerick Poet demo

This directory contains an example implementation of a real-time chat agent using the [Fishjam](https://fishjam.io) and [OpenAI Agents](https://github.com/openai/openai-agents-python) Python SDKs.

The agent introduces itself when the user joins and creates limericks based on what the user says.
The agent handles interruptions from users to ensure a natural conversation flow.

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
- `OPENAI_API_KEY`: An API key for the OpenAI Realtime API. You can generate one on the [OpenAI website](https://platform.openai.com/api-keys).

Once you have these variables, you can run the demo with

```bash
FISHJAM_ID=<your-fishjam-id> \
FISHJAM_MANAGEMENT_TOKEN=<your-management-token> \
GEMINI_API_KEY=<your-api-token> \
uv run ./main.py
```

A peer token should be generated and printed to standard output.
You can then use the [minimal-react](https://github.com/fishjam-cloud/web-client-sdk/tree/main/examples/react-client)
demo app to connect with this token and talk with the agent!
