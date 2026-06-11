from pathlib import Path
import zipfile
import shutil
import tempfile

def read_directory(dir):
    """Legge una directory ricorsivamente e restituisce tutti i file."""
    
    path = Path(dir)

    if not path.exists():
        print(f"La directory '{dir}' non esiste.")

    return [file for file in path.rglob("*") if file.is_file()]


def _build_file(file):
    """Prende un file, lo comprime in .zip, lo rinomina in .bin
    e lo copia in dokyll_temp mantenendo la struttura delle cartelle.
    """

    file = Path(file)

    if not file.exists():
        raise FileNotFoundError(file)

    # file.txt -> file.bin
    destination = Path("dokyll_temp") / file.with_suffix(".bin")

    # Crea le cartelle necessarie
    destination.parent.mkdir(parents=True, exist_ok=True)

    # Evita collisioni
    while destination.exists():
        destination = destination.with_name(f"dk.{destination.name}")

    # Zip temporaneo
    with tempfile.NamedTemporaryFile(suffix=".zip", delete=False) as tmp:
        zip_path = Path(tmp.name)

    try:
        with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zf:
            zf.write(file, arcname=file.name)

        # zip -> bin
        shutil.copy2(zip_path, destination)

    finally:
        if zip_path.exists():
            zip_path.unlink()

    return destination

def build_pages(project_name):
    """Fa la build delle pagine."""

    project_path = Path(project_name)

    # Legge la directory
    files = read_directory(project_path)

    # Fa la build di tutti i file della directory
    for file in files:
        _build_file(file)

    # Prende tutti i file in dokyll_temp e li comprime
    temp_dir = Path(f"dokyll_temp/{project_name}")

    zip_path = Path(f"{project_path.name}.zip")

    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zf:
        for file in temp_dir.rglob("*"):
            if file.is_file():
                zf.write(file, arcname=file.relative_to(temp_dir))

    # Rinomina .zip in .dok
    dok_path = zip_path.with_suffix(".dok")

    if dok_path.exists():
        dok_path.unlink()

    zip_path.rename(dok_path)

    # Se tutto è andato bene, mostra un messaggio di congratulazioni
    print(f"Congratulazioni! La tua build è disponibile in {dok_path}!")
