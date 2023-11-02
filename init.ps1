# Set-ExecutionPolicy -Scope CurrentUser ByPass -Force
& "g:/win32app/Portable Python-3.10.5 x64/App/Python/python.exe" -m venv env
./env/scripts/activate
python -m pip install --upgrade pip
python -m pip install pygame