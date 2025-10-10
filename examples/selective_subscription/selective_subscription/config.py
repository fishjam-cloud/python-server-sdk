import os

FISHJAM_ID = os.getenv("FISHJAM_ID", "")
FISHJAM_TOKEN = os.environ["FISHJAM_MANAGEMENT_TOKEN"]
FISHJAM_URL = os.getenv("FISHJAM_URL", "http://localhost:5002")
HOST = os.getenv("HOST", "localhost")
PORT = int(os.getenv("PORT", "8000"))