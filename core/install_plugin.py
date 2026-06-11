import requests
from pathlib import Path
import os

BASE_PATH = os.path.dirname(os.path.abspath(__file__))

PLUGINS_PATH = Path(os.path.abspath(os.path.join(BASE_PATH, "..", "plugins")))
PLUGINS_BASE_RAW = "https://github.com/dokyll/plugins-server/raw/refs/heads/main"


def progress_bar(downloaded, total, width=30):
    filled = int(width * downloaded / total)

    bar = "━" * filled + "─" * (width - filled)
    percent = downloaded / total * 100

    print(f"\r[{bar}] {percent:5.1f}%", end="", flush=True)


def install_plugin(plugin):
    PLUGINS_PATH.mkdir(parents=True, exist_ok=True)

    url = f"{PLUGINS_BASE_RAW}/{plugin}.exe"
    destination = PLUGINS_PATH / f"{plugin}.exe"

    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()
    except requests.RequestException:
        print("Plugin non trovato")
        return None

    total_size = int(response.headers.get("content-length", 0))
    downloaded = 0

    with open(destination, "wb") as f:
        for chunk in response.iter_content(chunk_size=8192):
            if chunk:
                f.write(chunk)

                downloaded += len(chunk)

                if total_size:
                    progress_bar(downloaded, total_size)

    print("\nPlugin installato correttamente.")
    return destination
