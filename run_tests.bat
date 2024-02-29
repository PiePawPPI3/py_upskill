@echo off
cd C:\Users\ppielka\PycharmProjects\pythonProject\
python -m pytest --cov=. --cov-report term-missing
pause