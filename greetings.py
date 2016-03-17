import urllib2
import sys
import gmail
import gcalendar
import weather
import time
import locale
import notif
from os import system

try:
    locale.setlocale(locale.LC_ALL,'fr_FR')
except:
    locale.setlocale(locale.LC_ALL,'')

system('say Bonjour Monsieur.')
system('say "Nous sommes le %s."' % (time.strftime ("%A %d %B %Y")))
system('say "Il est %s heure %s."' % (time.strftime("%H"),time.strftime("%M")))
system('say "%s"' % weather.main().encode('utf8'))
system('say "%s"' % gmail.main().encode('utf8'))
system('say "%s"' % gcalendar.main().encode('utf8'))