#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021/7/7 14:48
# @Author  : YOURNAME
# @FileName: reprint.py
# @Software: PyCharm
import os

rewrite_print = print


#  重写print，使其输出后存入文档
def print(*arg):
    rewrite_print(*arg)
    output_dir = "log"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        # print('新建log文件夹')
    log_name = 'log.txt'  # 日志文件名称
    filename = os.path.join(output_dir, log_name)
    rewrite_print(*arg, file=open(filename, "a"))  # 写入文件
