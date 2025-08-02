#!/bin/bash
set -e

echo "Проверяем Python3..."
if ! command -v python3 &>/dev/null; then
  echo "Python3 не найден. Пожалуйста, установите Python3 и повторите."
  exit 1
fi

echo "Проверяем pip..."
if ! python3 -m pip --version &>/dev/null; then
  echo "pip не найден. Устанавливаю pip..."
  python3 -m ensurepip --upgrade
fi

echo "Создаем виртуальное окружение .venv"
python3 -m venv .venv

echo "Активируем виртуальное окружение"
source .venv/bin/activate

echo "Обновляем pip"
pip install --upgrade pip

echo "Устанавливаем пакет github-activity в виртуальное окружение"
pip install .

BIN_DIR="$HOME/.local/bin"
mkdir -p "$BIN_DIR"

VENV_BIN="$(pwd)/.venv/bin/github-activity"

if [ -f "$VENV_BIN" ]; then
  ln -sf "$VENV_BIN" "$BIN_DIR/github-activity"
  echo "Создана ссылка: $BIN_DIR/github-activity"
else
  echo "Не удалось найти github-activity в виртуальном окружении"
  exit 1
fi

case ":$PATH:" in
  *":$BIN_DIR:"*) ;;
  *)
    export PATH="$PATH:$BIN_DIR"
    echo "Добавлен $BIN_DIR в PATH для текущей сессии"
    ;;
esac

echo "Установка завершена!"
echo "Теперь вы можете запускать CLI командой: github-activity"
echo "Если команда не найдена, добавьте $BIN_DIR в PATH в вашем профиле shell."
