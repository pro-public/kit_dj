#!/bin/bash

# Lista de módulos a verificar
modules=("spotipy" "requests" "python-dotenv" "tqdm")

# Verificar si pip está instalado
if ! command -v pip &> /dev/null; then
    echo "pip no está instalado. Por favor, instala pip primero."
    exit 1
fi

# Chequear e instalar los módulos faltantes
for module in "${modules[@]}"
do
    if ! python3 -c "import $module" &> /dev/null; then
        echo "El módulo $module no está instalado. Instalando..."
        pip install $module
        if [ $? -eq 0 ]; then
            echo "$module se ha instalado correctamente."
        else
            echo "Error instalando $module."
        fi
    else
        echo "El módulo $module ya está instalado."
    fi
done

