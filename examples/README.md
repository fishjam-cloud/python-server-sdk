# Fishjam Room Manager

## Running (in dev mode)

All available options are defined in [arguments.py](room_manager/arguments.py).

```console
uv sync --all-packages
uv run room_manager # Room Manager has to be started in the project root directory
```

## How does it work?

Fishjam Room Manager serves the purpose of a simple backend that allows users to create and/or join Fishjam rooms.
Users must provide a room name and their username to obtain an authentication token that allows them to connect to a Fishjam instance.
Room Manager manages the room names and user names by itself by keeping the mappings in memory.

As of now, it exposes 2 endpoints.

### '/api/rooms/:roomName/users/:username'

Returns authentication token for a username in a given room. If the user doesn't exist yet, it will be created.

### '/api/rooms/webhook'

Exposes a webhook endpoint to allow the Fishjam instance to send notifications to the Room Manager.
