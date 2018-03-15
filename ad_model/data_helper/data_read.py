# -*- coding: utf-8 -*-
"""
数据格式转化
Authors: yu
Date: 2018-3-15
"""

import os
import numpy
import pandas as pd

current_dir = os.path.dirname(os.path.abspath(__file__))
data_test_path = os.path.join(current_dir, "../data/test_file")

def data_clean():
    clean_list = [2, 3, 18]
    data = pd.read_table(data_test_path, header=None, encoding='gb2312', delim_whitespace=True)
    for list_num in clean_list:
        for i in range(len(data[list_num])):
            data[list_num][i] = data[list_num][i].split(';')
    data_list = data.T
    return data_list



if __name__ == '__main__':
    data_clean()

