import sys
from pathlib import Path
from rich.console import Console
from lib.common import run_command
from lib import config

console = Console()

def run(pkg: str, local: bool = False):
    pkg_dir = config.MODELS_DIR / pkg
    if not pkg_dir.exists():
        console.print(f"[red]✘ El paquete '{pkg}' no está instalado[/red]")
        sys.exit(1)

    if local:
        console.print("[cyan]→ Ejecutando 'make run-local'[/cyan]")
        run_command("make run-local", cwd=pkg_dir)
    else:
        console.print("[cyan]→ Ejecutando 'make run'[/cyan]")
        run_command("make run", cwd=pkg_dir)
