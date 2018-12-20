#!/usr/bin/python3

import os, sys
#import csv
import wechatsogou
import xlwt
from xlwt import Workbook

from conf import *

def gzh_history(name):
    ws_api = wechatsogou.WechatSogouAPI()
    print("正在抓取公众号：", name)
    gzh_hist = ws_api.get_gzh_article_by_history(name)
    file_name = "gzh_hist_" + name + ".xls"
    file_name = os.path.join(dir_name, file_name)
    print("正在写入文件:", file_name)
    gzh_article = gzh_hist['article']
    wb = Workbook()
    ws = wb.add_sheet('sheet1')
    colums = list(gzh_article[0].keys())
    for j, col in enumerate(colums):
        ws.write(0, j, col)
    for i, row in enumerate(gzh_article):
        for j, col in enumerate(colums):
            ws.write(i+1, j, row[col])
    wb.save(file_name)
    print("写入文件完成:", file_name)


def main():
    if (not os.path.isdir(dir_name)):
        os.mkdir(dir_name)

    print("抓取公众号的历史文章...")

    for name in gzh_name:
        gzh_history(name)




if __name__ == "__main__":
#    print(sys.getdefaultencoding())
    main()
