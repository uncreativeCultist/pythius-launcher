import dearpygui.dearpygui as dpg
from sys import platform
import os
from zipfile import ZipFile
import urllib.request
import shutil

if platform == "win32":
    needs_wine = 0
else:
    needs_wine = 1 #i mean its not windows so it probably needs wine


dpg.create_context()

def download():
    directory = dpg.get_value(item="directory")
    downloadurl = dpg.get_value(item="downloadurl")
    dpg.set_value("status", "Downloading...")
    urllib.request.urlretrieve(downloadurl, "temp.zip")
    if os.path.exists(directory):
        shutil.rmtree(directory)
    dpg.set_value("status", "Extracting...")
    with ZipFile("./temp.zip", 'r') as zObject:
        zObject.extractall(
                path=directory)
    os.remove("./temp.zip")
    dpg.set_value("status", "Done! Legacy Console Edition has been installed!")


def singleplayer():
    directory = dpg.get_value(item="directory")
    ipaddr = dpg.get_value(item="ipaddr")
    port = dpg.get_value(item="port")
    username = dpg.get_value(item="username")
    dpg.set_value("status", "Launching Legacy Console Edition...")
    if os.path.exists(f'{directory}servers.txt'):
        os.remove(f'{directory}servers.txt')
    with open(f'{directory}servers.txt', 'w') as file:
        file.write(f'{ipaddr}\n{port}\nConnect to server')
    if os.path.exists(f'{directory}username.txt'):
        os.remove(f'{directory}username.txt')
    with open(f"{directory}username.txt", "w") as f:
        f.write(f"{username}")
    if not os.path.exists(directory):
        dpg.set_value("status", "Unable to find game files! Is Legacy Console Edition installed?")
    elif not os.path.exists(f'{directory}Minecraft.Client.exe'):
        dpg.set_value("status", "Malformed or missing game files! Please reinstall Legacy Console Edition.")
    elif needs_wine == 1:
        os.system(f'cd {directory} && wine Minecraft.Client.exe -name "{username}"')
        dpg.set_value("status", "Ready!")
    else:
        os.system(f'cd {directory} && Minecraft.Client.exe -name "{username}"')
        dpg.set_value("status", "Ready!")

width, height, channels, data = dpg.load_image("./Resources/pythius.png")


with dpg.texture_registry(show=False):
    dpg.add_static_texture(width=width, height=height, default_value=data, tag="texture_tag")

with dpg.value_registry():
    dpg.add_string_value(default_value="PlayerName", tag="username")
    dpg.add_string_value(default_value="./GameFiles/", tag="directory")
    dpg.add_string_value(default_value="127.0.0.1", tag="ipaddr")
    dpg.add_string_value(default_value="25565", tag="port")
    dpg.add_string_value(default_value="https://github.com/smartcmd/MinecraftConsoles/releases/download/nightly/LCEWindows64.zip", tag="downloadurl")
    dpg.add_string_value(default_value="Ready!", tag="status")


with dpg.window(tag="Primary Window"):
    dpg.add_image("texture_tag", pos=(710, 10))
    dpg.add_text("Launcher Settings")
    dpg.add_input_text(label="Download Source", source="downloadurl", width=300)
    dpg.add_input_text(label="Directory", source="directory", width=260)
    dpg.add_button(label="Install Legacy Console Edition", callback=download)
    dpg.add_text(" ")
    dpg.add_text("Game Settings")
    
    
    dpg.add_input_text(label="Username", source="username", width=240)
    dpg.add_text(" ")
    dpg.add_text("Multiplayer Settings")
    dpg.add_input_text(label="IP Address", source="ipaddr", width=85)
    
    dpg.add_input_text(label="Port", source="port", width=45)
    
    dpg.add_button(label="Launch Minecraft: Legacy Console Edition", callback=singleplayer, width=330, pos=(439, 240))
    dpg.add_text(" ")
    dpg.add_text("Status:")
    dpg.add_text(source="status")

dpg.create_viewport(title="Pythius - @uncreativeCultist - v1.0.3a", width=784, height=361)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.set_primary_window("Primary Window", True)
dpg.start_dearpygui()
dpg.destroy_context()
