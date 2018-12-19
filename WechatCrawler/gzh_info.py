#!/usr/bin/python3

try:
    import wechatsogou
except ImportError as err:
    print("fail to import wechatsogou", err)
    print("please install wechatsogou")
    quit()

import os
import csv
from conf import *

def main():
    print("抓取公众号的基础信息...")

    gzh_info = []
    ws_api = wechatsogou.WechatSogouAPI()
    for name in gzh_name:
        print("正在抓取公众号：", name)
        info = ws_api.get_gzh_info(name)
        gzh_info.append(info)

    if (not os.path.isdir(dir_name)):
        os.mkdir(dir_name)

    csvfile_col = list(gzh_info[0].keys())
    csvfile_name = os.path.join (dir_name, "gzh_info.csv")

    print("正在写入文件:", csvfile_name)
    with open(csvfile_name, 'w') as csvfile:
        writer = csv.DictWriter(csvfile,
                            fieldnames=csvfile_col)
        writer.writeheader()
        for info in gzh_info:
            writer.writerow(info)

    print("写入文件完成:", csvfile_name)

if __name__ == "__main__":
    pass
    main()
