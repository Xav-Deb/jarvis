import urllib2
import sys
import gmail
import weather
import time

try:
    import locale
    locale.setlocale(locale.LC_ALL,'fr_FR')
except:
    locale.setlocale(locale.LC_ALL,'')

print 'Bonjour Monsieur.'
print 'Nous sommes le %s.' % (time.strftime ("%A %d %B %Y"))
print 'Il est %s heure %s.' % (time.strftime("%H"),time.strftime("%M"))
print weather.main()
print gmail.main()
