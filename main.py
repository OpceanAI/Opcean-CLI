import argparse
import os
from pathlib import Path
from rich.console import Console

from lib.common import run_command
from funcs.install import install
from funcs.remove import remove
from funcs.run import run
from funcs.update import update

console = Console()

def main():
    parser = argparse.ArgumentParser(description="Instalador de bots Docker uwu")
    parser.add_argument("--update", help="Actualizar keys.json desde URL")
    parser.add_argument("--install", help="Instalar paquete")
    parser.add_argument("--run", help="Ejecutar paquete instalado")
    parser.add_argument("--remove", help="Eliminar paquete instalado")
    args = parser.parse_args()

    if args.update:
        update(args.update)
    elif args.install:
        install(args.install)
    elif args.run:
        run(args.run)
    elif args.remove:
        remove(args.remove)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
