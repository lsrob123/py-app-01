Windows
cd C:\Experiment\Python\py-app-01

WSL
cd /mnt/c/Experiment/Python/py-app-01

Mac





@REM gunicorn -w 4 'app:app'

uvicorn main:app --host 0.0.0.0

uvicorn main:app --reload
