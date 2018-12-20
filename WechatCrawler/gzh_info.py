#!/usr/bin/python3

import os, sys
#import csv
import wechatsogou
import xlwt
from xlwt import Workbook

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

    file_name = os.path.join (dir_name, "gzh_info.xls")
    print("正在写入文件:", file_name)
    wb = Workbook()
    ws = wb.add_sheet('sheet1')
    colums = list(gzh_info[0].keys())
    for j, col in enumerate(colums):
        ws.write(0, j, col)
    for i, row in enumerate(gzh_info):
        for j, col in enumerate(colums):
            ws.write(i+1, j, row[col])
    wb.save(file_name)
    print("写入文件完成:", file_name)

if __name__ == "__main__":
    main()
