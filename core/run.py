import os
import subprocess

BASE_PATH = os.path.dirname(os.path.abspath(__file__))

PLUGINS_PATH = os.path.abspath(os.path.join(BASE_PATH, "..", "plugins"))

def run_plugin(plugin):
    exe_path = os.path.join(PLUGINS_PATH, f"{plugin}.exe")

    if not os.path.exists(exe_path):
        print("Plugin non trovato:", exe_path)
        return

    subprocess.run(exe_path, shell=True)
