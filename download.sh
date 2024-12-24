#!/bin/bash
echo "Chequeo de pre requisitos (librerias de python)"
./pre_reqs.sh
# Comprobar si existe the archivo this.txt
if [ -f "data/this.txt" ]; then
    rm data/this.txt
    python3 conv_nml-to-txt.py
else
    python3 conv_nml-to-txt.py
fi
echo "Contenido del archivo this.txt"
python3 read_txt.py ; sleep 2
python3 search_spotify.py ; sleep 2
clear ; echo "Ready at..." ; cat data/this.txt
