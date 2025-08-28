import sys, shutil
from pathlib import Path
from rich.console import Console
from lib.common import run_command

console = Console()

BASE_DIR = Path(__file__).resolve().parent.parent
MODELS_DIR = BASE_DIR / "models"
def remove(pkg: str):
    pkg_dir = MODELS_DIR / pkg
    if not pkg_dir.exists():
        console.print(f"[red]✘ El paquete '{pkg}' no está instalado[/red]")
        return

    console.print("[cyan]→ Ejecutando 'make uninstall'[/cyan]")
    run_command("make uninstall", cwd=pkg_dir)

    shutil.rmtree(pkg_dir)
    console.print(f"[green]✔ Paquete '{pkg}' eliminado[/green]")
