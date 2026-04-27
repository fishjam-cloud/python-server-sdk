# AGENTS.md

## Development workflow

### Red-Green TDD for new features

Whenever a new feature is added, follow the red-green TDD cycle:

1. **Red** — write a failing test that describes the desired behavior. Run it and confirm it fails for the expected reason.
2. **Green** — write the minimum production code needed to make the test pass. Run the test and confirm it passes.
3. **Refactor** — clean up the implementation and tests while keeping the suite green.

Do not write production code for a new feature before a failing test exists for it.
