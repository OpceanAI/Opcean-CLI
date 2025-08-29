import sys, json, requests
from pathlib import Path
from rich.console import Console
from rich.table import Table
from lib import config
from lib.common import run_command

console = Console()

def install(pkg: str):
    if not config.KEYS_FILE.exists():
        console.print("[red]✘ No existe keys.json, ejecuta --update primero[/red]")
        sys.exit(1)

    keys = json.loads(config.KEYS_FILE.read_text())
    if pkg not in keys:
        console.print(f"[red]✘ Paquete '{pkg}' no encontrado[/red]")
        sys.exit(1)

    # Descargar descriptor
    r = requests.get(keys[pkg])
    r.raise_for_status()
    desc = r.json()

    # Mostrar tabla con info
    table = Table(title=f"Información del paquete: {desc.get('name', pkg)}")
    table.add_column("Campo", style="cyan", no_wrap=True)
    table.add_column("Valor", style="magenta")
    
    for key, value in desc.items():
        if key != "makefile_url":  # no mostramos URL del Makefile
            table.add_row(key.capitalize(), str(value))
    
    console.print(table)

    # Preguntar si quiere instalar
    confirm = console.input("[yellow]¿Deseas instalar este paquete? (y/n) > [/yellow]")
    if confirm.lower() != "y":
        console.print("[red]✘ Instalación cancelada[/red]")
        return

    pkg_dir = config.MODELS_DIR / pkg
    pkg_dir.mkdir(parents=True, exist_ok=True)

    # Descargar Makefile
    makefile_url = desc["makefile_url"]
    makefile_content = requests.get(makefile_url).text
    (pkg_dir / "Makefile").write_text(makefile_content)

    console.print("[cyan]→ Ejecutando 'make install'[/cyan]")
    run_command("sudo make install", cwd=pkg_dir)
