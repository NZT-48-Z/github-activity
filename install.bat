@echo off
python -m venv .venv
call .venv\Scripts\activate
pip install --upgrade pip
pip install .
echo Установка завершена.
echo Чтобы запустить CLI, используйте команду "github-activity"
pause
