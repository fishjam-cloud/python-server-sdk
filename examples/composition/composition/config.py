import os

import dotenv

dotenv.load_dotenv()

FISHJAM_ID = os.environ["FISHJAM_ID"]
FISHJAM_TOKEN = os.environ["FISHJAM_MANAGEMENT_TOKEN"]
COMPOSITION_URL = os.getenv("COMPOSITION_URL")
HOST = os.getenv("HOST", "localhost")
PORT = int(os.getenv("PORT", "8000"))

CAMERA_INPUT_ID = "camera"
MOVIE_INPUT_ID = "movie"
LOGO_IMAGE_ID = "fish"
OUTPUT_ID = "livestream"

MOVIE_URL = "https://github.com/smelter-labs/smelter-snapshot-tests/raw/refs/heads/main/assets/BigBuckBunny720p24fpsStereo30s.mp4"
LOGO_URL = "https://fishjam.swmansion.com/favicon.svg"
FONT_URL = "https://raw.githubusercontent.com/google/fonts/main/ofl/inter/Inter%5Bopsz%2Cwght%5D.ttf"
FONT_FAMILY = "Inter"

WIDTH = 1280
HEIGHT = 720
