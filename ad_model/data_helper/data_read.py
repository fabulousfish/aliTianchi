# -*- coding: utf-8 -*-
"""
数据格式转化
Authors: yu
Date: 2018-3-15
"""

import os
import re
import traceback
import pandas as pd

current_dir = os.path.dirname(os.path.abspath(__file__))
data_path = os.path.join(current_dir, "../data/test_file")

def data_read():
    clean_list = [2, 3, 18]
    data = pd.read_table(data_path, header=None, encoding='gb2312', delim_whitespace=True)
    for list_num in clean_list:
        for i in range(len(data[list_num])):
            try:
                list_string = re.split('[:,;]', data[list_num][i])
                data[list_num][i] = list(map(int, list_string))
            except :
                traceback.print_exc()
                print(list_num, i)
    data_list = data.T
    return data_list


if __name__ == '__main__':
    data_list = data_read()

