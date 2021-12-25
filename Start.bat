@echo off
color 02

if exist "venv" (
	%~dp0\venv\scripts\activate
	py KeepAlive.py
) else (
	echo Setting up new environment, initial setup may take time based on your internet speed.
	echo Please wait...
	py -m venv venv
	%~dp0\venv\scripts\activate
	pip install pyautogui
	cls
	py KeepAlive.py
)
