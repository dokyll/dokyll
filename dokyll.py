"""
Dokyll Page Builder
"""

import sys
import os

BASE_PATH = os.path.dirname(os.path.abspath(__file__))

# aggiunge la root al path (utile per import)
sys.path.append(BASE_PATH)

import core.utils
import core.install_plugin
import core.run

def help_menu():
    print("Dokyll Page Builder")
    print("Versione dev 20260615\n")
    print("Comandi:")
    print("- dokyll build-pages [NOME_PROGETTO]")
    print("  Fa la build di un progetto.")
    print("  Il nome progetto deve coincidere con la directory.")
    print("- dokyll install-plugin [NOME_PLUGIN]")
    print("  Installa un plugin")
    print("- dokyll plugin [NOME_PLUGIN]")
    print("  Avvia un plugin.")


if len(sys.argv) < 2:
    help_menu()
    sys.exit(0)

command = sys.argv[1]

if command == "build-pages":
    if len(sys.argv) < 3:
        print("Errore: manca il nome del progetto")
        sys.exit(1)

    project = sys.argv[2]
    core.utils.build_pages(project)

elif command == "install-plugin":
    if len(sys.argv) < 3:
        print("Errore: manca il nome del plugin")
        sys.exit(1)
    
    plugin = sys.argv[2]
    core.install_plugin.install_plugin(plugin)

elif command == "plugin":
    if len(sys.argv) < 3:
        print("Errore: manca il nome del plugin")
        sys.exit(1)

    plugin = sys.argv[2]
    core.run.run_plugin(plugin)

elif command == "unzip":
    if len(sys.argv) < 3:
        print("Nome build mancante.")
        sys.exit(1)

    build = sys.argv[2]
    core.utils.unzip_build(build)

else:
    help_menu()
