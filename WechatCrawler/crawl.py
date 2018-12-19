#!/usr/bin/python3

try:
    import wechatsogou
except Exception as err:
    print("fail to import wechatsogou", err)
    quit()

from conf import *

gzh_info = []
ws_api = wechatsogou.WechatSogouAPI()
for name in gzh_name:
    info = ws_api.get_gzh_info(name)
    gzh_info.append(info)

#print(gzh_info)

with open('gzh_info.csv', 'wb') as f:  # Just use 'w' mode in 3.x
    w = csv.DictWriter(f, gzh_info.keys())
    w.writeheader()
    w.writerow(my_dict)


with open('gzh_info.txt', 'w') as file:
    file.write("gzh_info:")
    file.write(str(gzh_info))
