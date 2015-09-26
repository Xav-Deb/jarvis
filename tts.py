# coding: utf8
import pyttsx
import time
from pyowm import OWM
from notif import sendmessage
API_key = 'e1c56e2dfcb9660ac9cfdbf1dc0ccd99'
owm = OWM(API_key, version='2.5', language='fr')
obs = owm.weather_at_place('Lille,fr')
w = obs.get_weather()
meteo = u'Il est %s heure %s.\r\n' % (time.strftime("%H"),time.strftime("%M"))
meteo = meteo + u'Le temps est %s et la température est de %s degré.' % (w.get_detailed_status(), w.get_temperature(unit='celsius')['temp'])
sendmessage(meteo)
return(meteo)
#print w.get_reference_time(timeformat='iso')
#print w.get_temperature(unit='celsius')['temp']
#print w.get_detailed_status()

engine = pyttsx.init()
engine.setProperty('voice', 'french')
rate = engine.getProperty('rate')
engine.setProperty('rate', rate-50)
#voices = engine.getProperty('voices')
#for voice in voices:
#   print(voice.id)
#engine.say('Bonjour!')
#engine.say('Comment allez vous aujourd\'hui?')
engine.runAndWait()