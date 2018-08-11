# -*- coding: utf-8 -*-
"""
@author: James
"""
from xpinyin import Pinyin
import pandas as pd
p = Pinyin()
df = pd.read_csv('ChineseNames.csv')
p.get_pinyin()

#change headers to english
print(df.columns)

def strip_last_name(name):
    return name[1:]

