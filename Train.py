# -*- coding utf-8 -*-

import zipfile
from pprint import pprint

# zip_file_name = 'voyna-i-mir.txt.zip'
# zip_file = zipfile.ZipFile(zip_file_name, 'r')
# for filename in zip_file.namelist():
#     zip_file.extract(filename)
# '''раззиповали файл и вытащили в директорию, но кодировка не ютф8
# а cp1251'''
file_name = 'voyna-i-mir.txt'
stat = {}
# stat = {'a': {'т': 500, 'х': 5}, 'т': {'о': 100, 'у': 50}, }

prev_char = ' '

with open(file_name, 'r', encoding='cp1251') as file:
     for line in file:
         # print(line)
         for char in line:
             if prev_char in stat:
                 if char in stat[prev_char]:
                     stat[prev_char][char] += 1
                 else:
                     stat[prev_char][char] = 1
             else:
                 stat[prev_char] = {char : 1}
             prev_char = char
# pprint(stat)

totals = {}
stat_for_generate = {}

for prev_char, char_stat in stat.items():
    totals[prev_char] = 0
    stat_for_generate[prev_char] = []
    for char, count in char_stat.items():
        totals[prev_char] += count
        stat_for_generate[prev_char].append([count,char])
    stat_for_generate[prev_char].sort()

pprint(totals)
pprint(stat_for_generate)