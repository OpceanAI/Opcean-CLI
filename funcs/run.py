import sys
from pathlib import Path
from rich.console import Console
from lib.common import run_command

console = Console()

BASE_DIR = Path(__file__).resolve().parent.parent
MODELS_DIR = BASE_DIR / "models"

def run(pkg: str):
    pkg_dir = MODELS_DIR / pkg
    if not pkg_dir.exists():
        console.print(f"[red]✘ El paquete '{pkg}' no está instalado[/red]")
        sys.exit(1)

    console.print("[cyan]→ Ejecutando 'make run'[/cyan]")
    run_command("make run", cwd=pkg_dir)
