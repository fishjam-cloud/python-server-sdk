# Composition Demo

Demo application showing compositions, the real-time video compositing sessions, with
[Fishjam](https://fishjam.io) and the Python Server SDK.

Two sources are composed into one picture, laid out like a gaming livestream: a looping
movie fills the stage with your camera tucked into its top corner, framed by the Fishjam
logo and a caption bar. The result is sent to a Fishjam livestream that viewers watch.

```
[camera] ── WHIP ─┐
                  ├─▶ composition ── WHIP ─▶ fishjam livestream ── WHEP ─▶ [viewers]
[movie mp4] ──────┘
```

## What it shows

- **Inputs**: a WHIP input the demo prints publishing credentials for, and an MP4 input
  looping a movie from a URL
- **Renderers**: an SVG logo registered as an image, and the Inter font used by the caption
- **Scene**: the movie fills the stage with the camera in its top corner, on a cream frame
  with a coral bar along the bottom. Each tile sits on a black backing, so a stream that is
  not publishing yet reads as an empty tile rather than a hole
  - _picture in picture_ — the movie fills the stage, the camera sits in its top corner
  - _spotlight_ — the camera takes the stage with the movie tucked away
  - _side by side_ — the movie and the camera share the stage
- **Audio**: both inputs mixed, with the movie ducked under the camera

## Prerequisites

- Python 3.10+
- [uv](https://docs.astral.sh/uv/) package manager
- Fishjam credentials ([get them here](https://fishjam.io/app))

> [!IMPORTANT]
> All commands should be run from the `examples/composition` directory

## Quick Start

1. Install dependencies:

   ```bash
   uv sync
   ```

2. Copy [`.env.example`](./.env.example) to `.env` and populate your environment variables.

3. Run the server:

   ```bash
   uv run ./main.py
   ```

Starting the server creates the composition and the livestream, then serves two endpoints:

| Endpoint | Returns |
| --- | --- |
| `GET /streamer` | `url` and `token` to publish a camera into the composition over WHIP |
| `GET /viewer` | `url` and `token` to watch the composed result over WHEP |

Publish with any WHIP client, such as `useLivestreamStreamer` from the React client SDK,
and watch with a livestream viewer such as `useLivestreamViewer`.

Press Ctrl+C to delete the composition and the livestream room.

To change the scene while the output is running, call `CompositionClient.update_output`.
An update has to mirror the registration: this output registers both video and audio, so
an update has to carry both.

> [!NOTE]
> A composition holds resources until it is deleted, so let the demo clean up on exit
> rather than killing it.

## Composing a whole room

This demo composes inputs whose IDs it chooses itself. To compose everyone in a room
instead, forward the room's tracks with `FishjamClient.forward_room_tracks` and render
them with a template, since a template decides the layout as peers come and go. Build one
with `npx @fishjam-cloud/composition-cli build App.tsx --out template.js`, register it
with `CompositionClient.register_template_output`, and see the
[JS example](https://github.com/fishjam-cloud/js-server-sdk/tree/main/examples/composition)
for a template to start from.
