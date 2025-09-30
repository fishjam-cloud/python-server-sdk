import os
from pathlib import Path

import dotenv

from fishjam import AgentOptions, AgentOutputOptions, FishjamClient

dotenv.load_dotenv()

FISHJAM_ID = os.environ["FISHJAM_ID"]
FISHJAM_TOKEN = os.environ["FISHJAM_MANAGEMENT_TOKEN"]
FISHJAM_URL = os.getenv("FISHJAM_URL")

AGENT_OPTIONS = AgentOptions(output=AgentOutputOptions(audio_sample_rate=24000))

OPENAI_MODEL = "gpt-realtime"

PROMPT_DIR = Path(__file__).parents[1] / "prompts"

INSTRUCTION_PATH = PROMPT_DIR / "instructions.md"
GREET_PATH = PROMPT_DIR / "greet.md"

with open(INSTRUCTION_PATH) as prompt:
    OPENAI_INSTRUCTIONS = prompt.read()

with open(GREET_PATH) as prompt:
    OPENAI_GREET = prompt.read()

fishjam_client = FishjamClient(FISHJAM_ID, FISHJAM_TOKEN, fishjam_url=FISHJAM_URL)
