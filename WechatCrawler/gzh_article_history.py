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


def gzh_history(name):
    ws_api = wechatsogou.WechatSogouAPI()
    print("正在抓取公众号：", name)
    gzh_hist = ws_api.get_gzh_article_by_history(name)
    csvfile_name = "gzh_hist_" + name + ".csv"
    csvfile_name = os.path.join(dir_name, csvfile_name)
    print("正在写入文件:", csvfile_name)
    gzh_article = gzh_hist['article']
    csvfile_col = list(gzh_article[0].keys())
    with open(csvfile_name, 'w') as csvfile:
        writer = csv.DictWriter(csvfile,
                            fieldnames=csvfile_col)
        writer.writeheader()
        for info in gzh_article:
            writer.writerow(info)

    print("写入文件完成:", csvfile_name)


def main():
    if (not os.path.isdir(dir_name)):
        os.mkdir(dir_name)

    print("抓取公众号的历史文章...")

    for name in gzh_name:
        gzh_history(name)




if __name__ == "__main__":
    pass
    main()
