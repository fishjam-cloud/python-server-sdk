import os

FISHJAM_ID = os.environ["FISHJAM_ID"]
FISHJAM_MANAGEMENT_TOKEN = os.environ["FISHJAM_MANAGEMENT_TOKEN"]
WEBHOOK_SERVER_URL = os.getenv("WEBHOOK_SERVER_URL", "http://localhost:5000")
WEBHOOK_URL = f"{WEBHOOK_SERVER_URL}/webhook"
# Fishjam must reach the webhook server over the internet (CI exposes it through a
# tunnel and sets WEBHOOK_SERVER_URL); the localhost fallback is only reachable
# from the test process itself.
WEBHOOK_SERVER_PUBLIC = "WEBHOOK_SERVER_URL" in os.environ
