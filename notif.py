import subprocess, sys, feedparser
#Here, we import modules needed for this program

def sendmessage(message):
    subprocess.Popen(['notify-send', message])
    return
