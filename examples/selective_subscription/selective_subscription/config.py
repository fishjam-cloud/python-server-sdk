import os

FISHJAM_ID = os.environ["FISHJAM_ID"]
FISHJAM_TOKEN = os.environ["FISHJAM_MANAGEMENT_TOKEN"]
HOST = os.getenv("HOST", "localhost")
PORT = int(os.getenv("PORT", "8000"))
