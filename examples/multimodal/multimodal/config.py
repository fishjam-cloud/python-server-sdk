import os

from google.genai.types import Modality

FISHJAM_ID = os.getenv("FISHJAM_ID", "")
FISHJAM_TOKEN = os.environ["FISHJAM_MANAGEMENT_TOKEN"]

MULTIMODAL_MODEL = "gemini-2.5-flash-native-audio-preview-12-2025"

MULTIMODAL_CONFIG = {
    "response_modalities": [Modality.AUDIO],
    "thinking_config": {
        "include_thoughts": False,
    },
}

# Interval in seconds between image captures
IMAGE_CAPTURE_INTERVAL = float(os.getenv("IMAGE_CAPTURE_INTERVAL", "5.0"))
