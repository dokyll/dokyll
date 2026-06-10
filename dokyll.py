"""
Dokyll Page Builder
"""

import sys
import os

BASE_PATH = os.path.dirname(os.path.abspath(__file__))

# aggiunge la root al path (utile per import)
sys.path.append(BASE_PATH)

import core.utils


def help_menu():
    print("Dokyll Page Builder")
    print("Versione 1.0.0\n")
    print("Comandi:")
    print("- dokyll build-pages [NOME_PROGETTO]")
    print("  Fa la build di un progetto.")
    print("  Il nome progetto deve coincidere con la directory.")


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

else:
    help_menu()