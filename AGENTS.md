# AGENTS.md

## Development workflow

### Red-Green TDD for new features

Whenever a new feature is added, follow the red-green TDD cycle:

1. **Red** — write a failing test that describes the desired behavior. Run it and confirm it fails for the expected reason.
2. **Green** — write the minimum production code needed to make the test pass. Run the test and confirm it passes.
3. **Refactor** — clean up the implementation and tests while keeping the suite green.

Do not write production code for a new feature before a failing test exists for it.

## Cursor Cloud specific instructions

`uv` is pre-installed; the startup script runs `uv sync`. Non-obvious notes:

- Validated: `uv sync`, `uv run ruff check .`, and a smoke import (`uv run python -c "import fishjam"`).
- The `tests/` suite is integration-oriented: `tests/conftest.py` imports `FISHJAM_ID` and `FISHJAM_MANAGEMENT_TOKEN` at collection time, so `uv run pytest` fails with `KeyError` unless those env vars are set and a live Fishjam server is reachable. The unit-style tests run with placeholders, e.g. `FISHJAM_ID=dummy FISHJAM_MANAGEMENT_TOKEN=dummy uv run pytest tests/test_config_validation.py tests/test_allowed_notifications.py`.
