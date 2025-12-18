import os
import re
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
        "docker compose -f docker-compose-test.yaml up --build --remove-orphans test \
        --exit-code-from test"
    )
    check_exit_code("docker compose -f docker-compose-test.yaml down")


def run_local_test():
    check_exit_code('uv run pytest -m "not file_component_sources" -vv')


def run_formatter():
    check_exit_code("ruff format .")


def run_format_check():
    check_exit_code("ruff format . --check")


def run_linter():
    check_exit_code("ruff check .")


def run_linter_fix():
    check_exit_code("ruff check . --fix")


def generate_docs():
    here = Path(__file__).parent
    input = here / "doc"

    if input.exists():
        shutil.rmtree(input)

    check_exit_code(
        "pdoc \
    --include-undocumented \
    --favicon https://logo.swmansion.com/membrane/\\?width\\=100\\&variant\\=signetDark\
    --logo https://logo.swmansion.com/membrane/\\?width\\=70\\&variant\\=signetDark\
    -t templates/doc \
    -o doc \
    fishjam"
    )
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


def clean_mdx_content(content: str) -> str:
    parts = re.split(r"((?:```[\s\S]*?```|`[^`\n]+`))", content)

    # example: convert `fishjam._openapi_client.models.peer.Peer` into `Peer`
    internal_path_pattern = r"fishjam\.(?:[\w.]+\.)?_[\w.]+\."

    cleaned_parts = []
    for part in parts:
        if part.startswith("`"):
            text = (
                part.replace("&lt;", "<")
                .replace("&gt;", ">")
                .replace("&#39;", "'")
                .replace("builtins.", "")
            )

            text = re.sub(internal_path_pattern, "", text)

            cleaned_parts.append(text)
        else:
            text = part.replace("{", "\\{").replace("}", "\\}").replace("<", "&lt;")

            cleaned_parts.append(text)

    return "".join(cleaned_parts)


def generate_docusaurus():
    here = Path(__file__).parent
    input = here / "doc"
    out = here / "docusaurus"

    if input.exists():
        shutil.rmtree(input)
    if out.exists():
        shutil.rmtree(out)

    check_exit_code(
        "pdoc \
    --include-undocumented \
    -t templates/docusaurus \
    -o doc \
    fishjam"
    )
    try:
        os.remove(input / "index.html")
    except FileNotFoundError:
        pass

    out.mkdir(parents=True, exist_ok=True)

    for f in input.glob("**/*.html"):
        content = f.read_text(encoding="utf-8")
        safe_content = clean_mdx_content(content)
        rel_path = f.relative_to(input)
        dest_path = out / rel_path.parent / rel_path.stem / "index.md"
        dest_path.parent.mkdir(parents=True, exist_ok=True)

        dest_path.write_text(safe_content, encoding="utf-8")


def update_client():
    if len(sys.argv) < 2:
        raise RuntimeError("Missing fishjam openapi.yaml raw url positional argument")

    url_or_path = sys.argv[1]
    is_url = url_or_path.startswith("http://") or url_or_path.startswith("https://")
    file_arg = f"--url {url_or_path}" if is_url else f"--path {url_or_path}"

    check_exit_code(
        f"openapi-python-client generate \
            {file_arg} \
            --config openapi-python-client-config.yaml \
            --meta=none \
            --overwrite \
            --output-path=fishjam/_openapi_client/ \
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
