"""OSC client

This program sends OSC message to drive DMX lights,
each time you evaluate the code with "Ctrl + enter"

Need:
    - pythonosc ( pip install pythonosc)
    - keyboard (the pip version is buggy with Python3.7,
        so prefer 'git clone https://github.com/boppreh/keyboard' and after 'pip install .' )

In Troop, evaluate 'import light'

"""
import keyboard
from pythonosc import osc_message_builder
from pythonosc import udp_client

host = "127.0.0.1"
port = 57150
message = "Zbdm"

client = udp_client.SimpleUDPClient(host, port)

def sendlight(message):
    """Fonction to send with OSC a message"""
    client.send_message("/light", message)

### Hotkey "Ctrl + Enter"
keyboard.add_hotkey('ctrl+enter', sendlight, args=[message])
#keyboard.wait()
