#!/bin/sh

APP_NAME='g2u-airmedia';
APP_VERSION='0.3';
APP_ID='fr.freebox.g2u-airmedia';
FREEBOX_URL='http://mafreebox.freebox.fr/';
API_VERSION='api_version';
API_BASE_URL='api/';

LOGIN='login/';
LOGIN_AUTH='login/authorize/';
LOGIN_SESSION='login/session/';

AIRMEDIA_RECEIVERS = 'airmedia/receivers/';

API = {};
BASE_URL = '';
session_token = '';

resultCurl=$( mktemp )

curl -S -d "login=freebox&passwd=xunufroot" http://mafreebox.freebox.fr/login.php -v > $resultCurl 2>&1
if grep -q "Set-Cookie:" $resultCurl; then
    echo "Login to Freebox succeeded!"
else
    echo "Login to Freebox failed!"
    rm $resultCurl > /dev/null 2>&1
    exit 1
fi

csrfToken=`grep "X-FBX-CSRF-Token" $resultCurl | cut -f 3 -d ' ' | sed "s/\r//"  `
fbxSid=`grep "FBXSID" $resultCurl | cut -f 3 -d ' ' | sed "s/FBXSID=//" | sed "s/;//" | sed "s/\r//" `
curl -b  FBXSID=$fbxSid  --data-urlencode "csrf_token=${csrfToken}" -X POST -H "Content-Type: application/json" -d '{"action": "start", "media_type": "video", "media": "/home/vagrant/Vidéos/Alice-guitare.mp4", "password": "xunufroot"}' http://mafreebox.freebox.fr/api/v1/airmedia/receivers/Freebox%20Player/ > $resultCurl 2>&1
#curl -s -b FBXSID=$fbxSid -D - -o /dev/null -e http://mafreebox.freebox.fr/settings.php?page=wifi_conf http://mafreebox.freebox.fr/wifi.cgi --data-urlencode "csrf_token=${csrfToken}" -d "channel=11&ht_mode=disabled&method=wifi.ap_params_set&config=Valider" -H "X-Requested-With: XMLHttpRequest" -H "Accept: application/json, text/javascript, */*" -H "Content-Type: application/x-www-form-urlencoded; charset=UTF-8" > $resultCurl 2>&1
if grep -q "HTTP/1.1 200 OK" $resultCurl; then
    echo "Playing Video on Freebox succeeded!"
else
    echo "Playing Video on Freebox failed!"
    cat $resultCurl;
fi

rm $resultCurl > /dev/null 2>&1
echo "Logout to Freebox succeeded!"

exit 0