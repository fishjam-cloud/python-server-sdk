import os
import shutil
import json
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


HERE = Path(__file__).parent
SRC_DIR = HERE / "docusaurus"
DEST_DIR = HERE / "docusaurus-api"
DOC_ID_PREFIX = "api/server-python/"


def sanitize_name(name):
    """
    Sanitizes filenames and folder names.
    Crucially: converts '__init__' to 'index' to avoid 'init__'
    """
    if name.startswith("__init__"):
        if name == "__init__":
            return "index"
        return "index" + name[8:]

    return name.lstrip('_')

def sanitize_md_content(content):
    """
    Fixes MDX compilation errors caused by pydoc-markdown output.
    """
    return content.replace("{&#x27;", "\\{&#x27;").replace("&#x27;}", "&#x27;\\}")

def sanitize_path_string(path_str):
    """
    Sanitizes a full path string found in sidebar.json ID.
    """
    parts = path_str.split('/')
    clean_parts = []
    for p in parts:
        if p == "__init__":
            clean_parts.append("index")
        else:
            clean_parts.append(p.lstrip('_'))
    return '/'.join(clean_parts)

def clean_label(label):
    """
    Makes sidebar labels readable.
    e.g. "_openapi_client.api.room" -> "openapi_client.api.room"
    """
    if not label: 
        return label
    return label.lstrip('_')

def recursive_sidebar_update(item):
    """
    Traverses sidebar to clean IDs and Labels.
    """
    if isinstance(item, list):
        return [recursive_sidebar_update(i) for i in item]

    if isinstance(item, dict):
        if "id" in item and isinstance(item["id"], str):
            item["id"] = DOC_ID_PREFIX + sanitize_path_string(item["id"])

        if "label" in item and isinstance(item["label"], str):
            item["label"] = clean_label(item["label"])

        if "type" in item and item["type"] == "category" and "items" not in item:
             item["type"] = "doc"

        # Recurse
        if "items" in item:
            item["items"] = recursive_sidebar_update(item["items"])
            
        return item

    if isinstance(item, str):
        return {
            "type": "doc",
            "id": DOC_ID_PREFIX + sanitize_path_string(item)
        }
    
    return item


def generate_docusaurus():
    check_exit_code("pydoc-markdown")

    if DEST_DIR.exists():
        shutil.rmtree(DEST_DIR)

    print(f"Processing files from {SRC_DIR} to {DEST_DIR}...")

    for root, dirs, files in os.walk(SRC_DIR):
        root_path = Path(root)
        rel_path = root_path.relative_to(SRC_DIR)

        clean_parts = []
        for p in rel_path.parts:
            if p == "__init__":
                clean_parts.append("index")
            else:
                clean_parts.append(p.lstrip('_'))
        
        clean_rel_path = Path(*clean_parts)
        current_dest_dir = DEST_DIR / clean_rel_path
        current_dest_dir.mkdir(parents=True, exist_ok=True)

        for file in files:
            src_file = root_path / file
            clean_filename = sanitize_name(file)
            dest_file = current_dest_dir / clean_filename

            try:
                with open(src_file, 'r', encoding='utf-8') as f_in:
                    raw_content = f_in.read()

                clean_content = sanitize_md_content(raw_content)

                with open(dest_file, 'w', encoding='utf-8') as f_out:
                    f_out.write(clean_content)

            except Exception as e:
                print(f"Error processing {src_file}: {e}")

    root_index = DEST_DIR / "reference" / "index.md"

    if not root_index.parent.exists():
        root_index = DEST_DIR / "index.md"

    if not root_index.exists():
        print(f"Creating missing index at {root_index}")
        root_index.parent.mkdir(parents=True, exist_ok=True)
        with open(root_index, "w") as f:
            f.write("---\ntitle: API Reference\nsidebar_position: 1\n---\n\n# Python API Reference\n\nWelcome to the Server SDK documentation.")

    sidebar_path = DEST_DIR / "sidebar.json"
    if not sidebar_path.exists():
        found = list(DEST_DIR.rglob("sidebar.json"))
        if found: sidebar_path = found[0]

    if sidebar_path.exists():
        print(f"Cleaning sidebar at {sidebar_path}...")
        with open(sidebar_path, 'r', encoding='utf-8') as f:
            sidebar_data = json.load(f)

        clean_sidebar = recursive_sidebar_update(sidebar_data)
        
        with open(sidebar_path, 'w', encoding='utf-8') as f:
            json.dump(clean_sidebar, f, indent=2)
        print("Sidebar cleaned.")

    print("Removing temporary source directory...")
    if SRC_DIR.exists():
        shutil.rmtree(SRC_DIR)

    print("Done! ✅")


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
