#!/bin/bash

set -e 

python3 -m venv .venv

source .venv/bin/activate

pip install --upgrade pip

pip install --user pipx

pipx install .

echo "Установка завершена."
echo "Чтобы запустить CLI, используйте команду 'github-activity'"
