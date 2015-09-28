# coding: utf8
import time
from pyowm import OWM
def main():
	API_key = 'e1c56e2dfcb9660ac9cfdbf1dc0ccd99'
	owm = OWM(API_key, version='2.5', language='fr')
	obs = owm.weather_at_place('Lille,fr')
	w = obs.get_weather()
	#meteo = u'Il est %s heure %s.\n' % (time.strftime("%H"),time.strftime("%M"))
	meteo = u'Sur Lille, le temps est %s et la température est de %s degré.\n' % (w.get_detailed_status(), w.get_temperature(unit='celsius')['temp'])
	return(meteo)
if __name__ == '__main__':
    main()