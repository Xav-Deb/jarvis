import urllib2
import sys
import gmail
import weather
import time

lang = "fr"

print 'Bonjour Monsieur.'
print 'Nous sommes le %s %s %s.' % (time.strftime("%d"),time.strftime("%m"),time.strftime("%y"))
print 'Il est %s heure %s.' % (time.strftime("%H"),time.strftime("%M"))
print weather.main()
print gmail.main()
