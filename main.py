import datetime
import time
import os
import threading

# import to hide the cmd when its run
import ctypes
import win32gui, win32con

# The max time to keep the pc turned on
flagTime = "12:01 AM"



def background():
    while True:
        cTime = datetime.datetime.now().strftime("%I:%M %p")
        time.sleep(1)
        print(cTime)
        if(cTime >= flagTime):
            os.system("shutdown /s /t 1")

if __name__ == "__main__":
    
    # Hiding cmd and making it completely background app
    hide = win32gui.GetForegroundWindow()
    ctypes.windll.user32.ShowWindow( ctypes.windll.kernel32.GetConsoleWindow(), 6 )
    win32gui.ShowWindow(hide , win32con.SW_HIDE)

    # Running the thread
    threading.Thread(name='background', target=background).start()