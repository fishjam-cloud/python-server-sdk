# Limerick Poet demo

This directory contains an example implementation of a real-time chat agent using the [Fishjam](https://fishjam.io) and [OpenAI Agents](https://github.com/openai/openai-agents-python) Python SDKs.

The agent introduces itself when the user joins and creates limericks based on what the user says.
The agent handles interruptions from users to ensure a natural conversation flow.

## Running

> [!IMPORTANT]
> All commands should be run from the `examples/poet_chat` directory

Make sure to [install uv](https://docs.astral.sh/uv/getting-started/installation/) if you don't have it already.
Once you have `uv` installed, fetch the dependencies with

```bash
uv sync
```

To run the app, first copy [`.env.example`](./.env.example) to `.env` and populate your environment variables.

Once you have populated `.env`, you can run the demo with

```bash
uv run ./main.py
```

A peer token should be generated and printed to standard output.
You can then use the [minimal-react](https://github.com/fishjam-cloud/web-client-sdk/tree/main/examples/react-client)
demo app to connect with this token and talk with the agent!
