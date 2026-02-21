@echo off

uv venv .venv
call .venv\Scripts\activate.bat
uv pip install pyinstaller
pyinstaller --onefile --name emv cli.py
