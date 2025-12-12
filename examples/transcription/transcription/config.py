import os

from google.genai.types import AudioTranscriptionConfig, LiveConnectConfig, Modality

FISHJAM_ID = os.getenv("FISHJAM_ID", "")
FISHJAM_TOKEN = os.environ["FISHJAM_MANAGEMENT_TOKEN"]
TRANSCRIPTION_MODEL = "gemini-2.5-flash-native-audio-preview-09-2025"
TRANSCRIPTION_CONFIG = LiveConnectConfig(
    response_modalities=[Modality.AUDIO],
    input_audio_transcription=AudioTranscriptionConfig(),
)
