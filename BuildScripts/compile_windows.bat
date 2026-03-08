@echo off
cd ../
pyinstaller --noconfirm --hidden-import dearpygui --hidden-import discord-rich-presence --windowed --icon "./Resources/pythius.ico"  "./pythius.py"