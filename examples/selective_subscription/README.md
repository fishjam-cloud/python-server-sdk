# Selective Subscription Demo

Demo application showing selective subscription functionality with [Fishjam](https://fishjam.io) and the Python Server SDK.

## Prerequisites

- Python 3.11+
- [uv](https://docs.astral.sh/uv/) package manager
- Fishjam credentials ([get them here](https://fishjam.io/app))

> [!IMPORTANT]
> All commands should be run from the `examples/selective_subscription` directory

## Quick Start

1. Install dependencies (in the `examples/selective_subscription` directory):
   ```bash
   uv sync
   ```

To run the app, first copy [`.env.example`](./.env.example) to `.env` and populate your environment variables.

Once you have populated `.env`, you can run the demo with

2. Run the server:
   ```bash
   uv run ./main.py
   ```

3. Open http://localhost:8000 in your browser

You create peers using the web UI at [http://localhost:8000](http://localhost:8000).

1. Create peers with names
2. Copy peer tokens and use them with a WebRTC client (e.g., [minimal-react](https://github.com/fishjam-cloud/web-client-sdk/tree/main/examples/react-client/minimal-react))
3. Once peers have tracks, manage subscriptions through the web interface

### API Endpoints

- `POST /api/peers` - Create a peer with manual subscription mode
- `POST /api/subscribe_peer` - Subscribe to all tracks from a peer
- `POST /api/subscribe_tracks` - Subscribe to specific track IDs

