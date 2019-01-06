"""OSC client

This program sends OSC messages to drive DMX lights,
each time you evaluate the code with "Ctrl + enter"

And OSC messages for video switching

Need:
    - pythonosc ( pip install pythonosc)
    - keyboard (the pip version is buggy with Python3.7 but you can try with <3.7,
        so prefer 'git clone https://github.com/boppreh/keyboard' and after 'pip install .' )

In Troop:

from light import *

video(1) ### Envoie un message OSC (bien définir le host/port) : /video 1
         ### Est équivalent à ctrl + 1
         ### Les touches de Ctrl + 0 à Ctrl + 9 sont mappés sur l'envoie /video [1..10]


"""
import keyboard
from pythonosc import osc_message_builder
from pythonosc import udp_client

host = "127.0.0.1"
port = 57150
message = "Zbdm"

client = udp_client.SimpleUDPClient(host, port)

def sendlight(message):
    """Fonction to send with OSC a light message"""
    client.send_message("/light", message)

def video(video_msg):
    """Fonction du send with OSC a video message"""
    client.send_message("/video",video_msg)


### Hotkey "Ctrl + Enter"
keyboard.add_hotkey('ctrl+enter', sendlight, args=[message])
keyboard.add_hotkey('ctrl+1', video, args=[1])
keyboard.add_hotkey('ctrl+2', video, args=[2])
keyboard.add_hotkey('ctrl+3', video, args=[3])
keyboard.add_hotkey('ctrl+4', video, args=[4])
keyboard.add_hotkey('ctrl+5', video, args=[5])
keyboard.add_hotkey('ctrl+6', video, args=[6])
keyboard.add_hotkey('ctrl+7', video, args=[7])
keyboard.add_hotkey('ctrl+8', video, args=[8])
keyboard.add_hotkey('ctrl+9', video, args=[9])
keyboard.add_hotkey('ctrl+0', video, args=[10])
#keyboard.wait()
