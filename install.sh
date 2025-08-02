#!/bin/bash
set -e

pip install --upgrade pip

pip install --user pipx

pipx install .

echo "Установка завершена."
echo "Чтобы запустить CLI, используйте команду 'github-activity'"
