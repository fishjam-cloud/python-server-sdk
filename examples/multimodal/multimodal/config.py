import os

from google.genai.types import AudioTranscriptionConfig, LiveConnectConfig, Modality

FISHJAM_ID = os.getenv("FISHJAM_ID", "")
FISHJAM_TOKEN = os.environ["FISHJAM_MANAGEMENT_TOKEN"]

MULTIMODAL_MODEL = "gemini-2.5-flash-native-audio-preview-12-2025"

# MULTIMODAL_CONFIG = LiveConnectConfig(
#     response_modalities=[Modality.TEXT],
#     system_intruction="You are a real-time assistant. Describe what you see and hear.",
# )

MULTIMODAL_CONFIG = {
    "response_modalities": [Modality.AUDIO],
    "thinking_config": {
        "include_thoughts": False,
    },
    # "system_intruction": "You are a real-time assistant. Describe what you see and hear.",
}

# Interval in seconds between image captures
IMAGE_CAPTURE_INTERVAL = float(os.getenv("IMAGE_CAPTURE_INTERVAL", "5.0"))
