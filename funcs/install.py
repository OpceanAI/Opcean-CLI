import sys, json, requests
from pathlib import Path
from rich.console import Console
from lib.common import run_command

console = Console()

BASE_DIR = Path(__file__).resolve().parent.parent
MODELS_DIR = BASE_DIR / "models"
KEYS_FILE = BASE_DIR / "keys.json"

def install(pkg: str):
    """Instala un paquete buscándolo en keys.json"""
    if not KEYS_FILE.exists():
        console.print("[red]✘ No existe keys.json, ejecuta --update primero[/red]")
        sys.exit(1)

    keys = json.loads(KEYS_FILE.read_text())
    if pkg not in keys:
        console.print(f"[red]✘ Paquete '{pkg}' no encontrado[/red]")
        sys.exit(1)

    # Obtener descriptor JSON
    console.print(f"[yellow]→ Descargando descriptor de {pkg}...[/yellow]")
    r = requests.get(keys[pkg])
    r.raise_for_status()
    desc = r.json()

    pkg_dir = MODELS_DIR / pkg
    pkg_dir.mkdir(parents=True, exist_ok=True)

    # Descargar Makefile
    console.print("[yellow]→ Descargando Makefile...[/yellow]")
    makefile_url = desc["makefile_url"]
    makefile_content = requests.get(makefile_url).text
    (pkg_dir / "Makefile").write_text(makefile_content)

    console.print("[cyan]→ Ejecutando 'make install'[/cyan]")
    run_command("make install", cwd=pkg_dir)
