import os
import shutil
import subprocess
import sys
from pathlib import Path


def check_exit_code(command):
    process = subprocess.Popen(
        command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT
    )

    if not process.stdout:
        raise RuntimeError("Process has no STDOUT")

    while True:
        output = process.stdout.readline()
        if output == b"" and process.poll() is not None:
            break
        if output:
            print(str(output.strip(), "utf-8"))
    exit_code = process.poll()
    if exit_code != 0:
        sys.exit(exit_code)


def run_tests():
    check_exit_code("docker rm -f fishjam")
    check_exit_code("docker compose -f docker-compose-test.yaml pull")
    check_exit_code(
        "docker compose -f docker-compose-test.yaml up --remove-orphans test \
        --exit-code-from test"
    )
    check_exit_code("docker compose -f docker-compose-test.yaml down")


def run_local_test():
    check_exit_code('poetry run pytest -m "not file_component_sources" -vv')


def run_formatter():
    check_exit_code("ruff format .")


def run_format_check():
    check_exit_code("ruff format . --check")


def run_linter():
    check_exit_code("ruff check .")


def run_linter_fix():
    check_exit_code("ruff check . --fix")


def generate_docs():
    check_exit_code(
        "pdoc \
    --include-undocumented \
    --favicon https://logo.swmansion.com/membrane/\\?width\\=100\\&variant\\=signetDark\
    --logo https://logo.swmansion.com/membrane/\\?width\\=70\\&variant\\=signetDark\
    -t templates/doc \
    -o doc \
    fishjam"
    )
    here = Path(__file__).parent
    input = here / "doc"
    input_images = here / "images"
    out = here / "docs" / "api"
    out_images = here / "docs" / "api" / "images"

    if out.exists():
        shutil.rmtree(out)

    shutil.copytree(input, out)
    shutil.copytree(input_images, out_images)

    # ...and rename the .html files to .md so that mkdocs picks them up!
    for f in out.glob("**/*.html"):
        f.rename(f.with_suffix(".md"))


def update_client():
    if len(sys.argv) < 2:
        raise RuntimeError("Missing fishjam openapi.yaml raw url positional argument")

    check_exit_code(
        f"openapi-python-client update \
            --url {sys.argv[1]} \
            --config openapi-python-client-config.yaml \
            --custom-template-path=templates/openapi"
    )


def start_room_manager():
    current_path = os.getcwd()
    current_folder = os.path.basename(current_path)

    if current_folder != "python-server-sdk":
        raise RuntimeError(
            "Room Manager has to be started from the `python-server-sdk` directory."
        )

    subprocess.run(
        ["python", "-m", "examples.room_manager.main"] + sys.argv[1:], check=False
    )
