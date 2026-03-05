@echo off
cd ../
pyinstaller --noconfirm --hidden-import dearpygui --windowed --icon "./Resources/pythius.ico"  "./pythius.py"