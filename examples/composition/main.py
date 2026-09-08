import uvicorn
from composition.app import app
from composition.config import HOST, PORT

if __name__ == "__main__":
    print(f"streamer credentials on http://{HOST}:{PORT}/streamer")
    print(f"viewer token on http://{HOST}:{PORT}/viewer")
    uvicorn.run(app, host=HOST, port=PORT, log_level="info")
