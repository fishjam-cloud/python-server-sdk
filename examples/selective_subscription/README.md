# Selective Subscription Demo

Demo application showing selective subscription functionality with [Fishjam](https://fishjam.io) and the Python Server SDK.

## Prerequisites

- Python 3.11+
- [uv](https://docs.astral.sh/uv/) package manager
- Fishjam credentials ([get them here](https://fishjam.io/app))

## Quick Start

1. Install dependencies(in project root):
   ```bash
   uv sync
   ```

2. Run the server:
   ```bash
   FISHJAM_ID=<your-id> \
   FISHJAM_MANAGEMENT_TOKEN=<your-token> \
   uv run examples/selective_subscription/main.py
   ```

3. Open http://localhost:8000 in your browser

## Usage

1. Create peers with names
2. Copy peer tokens and use them with a WebRTC client (e.g., [minimal-react](https://github.com/fishjam-cloud/web-client-sdk/tree/main/examples/react-client/minimal-react))
3. Once peers have tracks, manage subscriptions through the web interface

### API Endpoints

- `POST /api/peers` - Create a peer with manual subscription mode
- `POST /api/subscribe_peer` - Subscribe to all tracks from a peer
- `POST /api/subscribe_tracks` - Subscribe to specific track IDs

