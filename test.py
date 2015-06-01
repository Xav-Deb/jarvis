import urllib2
import sys

lang = "fr"
text = sys.argv[1]

url = "http://translate.google.com/translate_tts?tl=%s&q=%s" % (lang,text)
print(url)
request = urllib2.Request(url)
request.add_header('User-agent', 'Mozilla/5.0') 
opener = urllib2.build_opener()

f = open("data.mp3", "wb")
f.write(opener.open(request).read())
f.close()