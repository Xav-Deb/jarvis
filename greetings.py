import urllib2
import sys
import gmail
import weather
import time
import locale

locale.setlocale(locale.LC_ALL,'')

lang = "fr"

print 'Bonjour Monsieur.'
print 'Nous sommes le ' + time.strftime ("%A %d %B %Y") #%s %s %s.' % (time.strftime("%A"),time.strftime("%d"),time.strftime("%B"),time.strftime("%Y"))
print 'Il est %s heure %s.' % (time.strftime("%H"),time.strftime("%M"))
print weather.main()
print gmail.main()
