#!/bin/sh

# comprobamos que tenga los paquetes necesarios instalados
# sudo apt update && sudo apt upgrade -y && sudo apt install python3 docker docker-compose make -y
sudo pacman -Syu --no-confirm && sudo pacman -S python3 docker docker-compose make --no-confirm

# creacion de la carpeta
mkdir opcean-cli && cd opcean-cli

# creacion de los directorios necesarios
mkdir models && mkdir lib && mkdir funcs && mkdir keys

# descarga de los archivos necesarios
curl -O https://raw.githubusercontent.com/OpceanAI/Opcean-CLI/refs/heads/main/requirements.txt
curl -O https://raw.githubusercontent.com/OpceanAI/Opcean-CLI/refs/heads/main/main.py

cd lib
curl -O https://raw.githubusercontent.com/OpceanAI/Opcean-CLI/refs/heads/main/lib/common.py
cd ..

cd funcs
curl -O https://raw.githubusercontent.com/OpceanAI/Opcean-CLI/refs/heads/main/funcs/install.py
curl -O https://raw.githubusercontent.com/OpceanAI/Opcean-CLI/refs/heads/main/funcs/run.py
curl -O https://raw.githubusercontent.com/OpceanAI/Opcean-CLI/refs/heads/main/funcs/remove.py
curl -O https://raw.githubusercontent.com/OpceanAI/Opcean-CLI/refs/heads/main/funcs/update.py
cd ..

# pip
python3 -m venv venv && source venv/bin/activate && pip install -r requirements.txt

# clonamos el archivo de configuracion por defecto
# curl -O https://raw.githubusercontent.com/OpceanAI/Opcean-CLI/refs/heads/main/default.config.json