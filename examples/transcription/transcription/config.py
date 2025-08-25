import os

from google.genai.types import AudioTranscriptionConfig, LiveConnectConfig, Modality

FISHJAM_ID = os.getenv("FISHJAM_ID", "")
FISHJAM_TOKEN = os.environ["FISHJAM_MANAGEMENT_TOKEN"]
FISHJAM_URL = os.getenv("FISHJAM_URL")
TRANSCRIPTION_MODEL = "gemini-live-2.5-flash-preview"
TRANSCRIPTION_CONFIG = LiveConnectConfig(
    response_modalities=[Modality.TEXT],
    input_audio_transcription=AudioTranscriptionConfig(),
)
