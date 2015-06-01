#!/usr/bin/env python
# -*- coding: utf-8 -*-
from subprocess import *
from os.path import expanduser
from threading import Thread
import sys, subprocess, os, json, unicodedata, time, locale, logging, requests, SimpleHTTPServer, SocketServer
from urllib2 import urlopen
from FreeboxAPI import FreeboxApplication

AppToken=expanduser('~') + '/.config/google2ubuntu/AppFreebox.token'
APP_NAME='google2ubuntu-airmedia'
APP_VERSION='0.1'
APP_ID='fr.freebox.google2ubuntu-airmedia'
FREEBOX_URL='http://mafreebox.freebox.fr/'
API_VERSION='api_version'
API_BASE_URL='api/'
LOGIN='login/'
LOGIN_AUTH='login/authorize/'
LOGIN_SESSION='login/session/'
AIRMEDIA_RECEIVERS='airmedia/receivers/'
AIRMMEDIA_DEVICE='Freebox Player'
API=''
BASE_URL=''

obj = requests.get(FREEBOX_URL + API_VERSION)
decoded = json.loads(obj.content)
API_V =  decoded['api_version'].split(".")[0]

locale.setlocale(locale.LC_ALL, '')
lang = locale.getdefaultlocale()[0]
lang=lang.split('_')[0]

sys.path.append('/usr/share/google2ubuntu/librairy')
from Googletts import tts

aLogFileToUse=(expanduser('~') + '/.config/google2ubuntu/AppFreebox.log')
#Clean previous log file
with open(aLogFileToUse, 'w'):
    pass
logging.basicConfig(filename=aLogFileToUse,level=logging.DEBUG,format='%(asctime)s - %(levelname)s - %(message)s')

G2U = FreeboxApplication(APP_ID, APP_NAME, APP_VERSION, 'ubuntu-laptop')

session_token=G2U.loginfull()

PORT = 8080

Handler = SimpleHTTPServer.SimpleHTTPRequestHandler

#httpd = SocketServer.TCPServer(("", PORT), Handler)

def serve_on_port(port):
    server = SocketServer.TCPServer(("", port), Handler)
    server.serve_forever()

os.chdir(expanduser('~') + '/Vidéos')
Thread(target=serve_on_port, args=[PORT]).start()
print "serving at port", PORT
#httpd.serve_forever()

params = {'action': 'start','media_type': 'video','media': 'http://192.168.100.24:'+ str(PORT) +'/Alice-guitare.mp4 ','password': ''}
#paramString = json.loads(params);
print ("params is : " + str(params) + str(session_token))
aRequestUrl = FREEBOX_URL + API_BASE_URL + 'v' + API_V + '/' + AIRMEDIA_RECEIVERS + AIRMMEDIA_DEVICE
logging.info("aRequestUrl is : " + str(aRequestUrl))
aHeaders = {"'X-Fbx-App-Auth': "+ str(session_token) +" , 'Content-type': 'application/json'"}
print (str(aHeaders))
logging.info("aHeaders is : " + str(aHeaders))
aRequestResult = requests.post(aRequestUrl, data=params, headers=aHeaders)