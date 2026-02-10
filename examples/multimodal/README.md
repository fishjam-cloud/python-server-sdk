# Multimodal Demo

A Fishjam SDK example that uses the Gemini Live API for multimodal real-time interaction. Users can speak to ask questions about captured video frames, and Gemini responds via voice.

## How It Works

1. A peer connects with both audio and video tracks
2. The agent periodically captures images from video tracks
3. When you speak ("What do you see?", "Describe this"), your audio and the captured images are sent to Gemini
4. Gemini analyzes the visual content and responds with voice

## Setup

1. Set environment variables:

```bash
export FISHJAM_ID="your-fishjam-id"
export FISHJAM_MANAGEMENT_TOKEN="your-token"
export GOOGLE_API_KEY="your-gemini-api-key"
```

2. Optionally configure the image capture interval (default: 5 seconds):

```bash
export IMAGE_CAPTURE_INTERVAL="3.0"
```

## Running

```bash
cd examples/multimodal
uv run uvicorn main:app
```

## Usage

1. The server will start on `http://localhost:8000`
2. GET `/` returns a peer token for connecting a browser client
3. Connect a peer with video and audio tracks
4. Speak questions about what your camera sees
5. Gemini will respond with voice analysis of the captured frames
