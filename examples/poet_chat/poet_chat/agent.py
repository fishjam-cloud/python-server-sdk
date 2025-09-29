from agents.realtime import RealtimeAgent, RealtimeRunner

from poet_chat.config import OPENAI_INSTRUCTIONS

poet = RealtimeAgent(name="Poet", instructions=OPENAI_INSTRUCTIONS)
poet_runner = RealtimeRunner(
    starting_agent=poet,
    config={
        "model_settings": {
            "voice": "alloy",
            "modalities": ["audio", "text"],
            "input_audio_format": "pcm16",
            "output_audio_format": "pcm16",
            "turn_detection": {
                "type": "semantic_vad",
            },
        }
    },
)
