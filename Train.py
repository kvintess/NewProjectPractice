# -*- coding utf-8 -*-
import random
import zipfile
from pprint import pprint

# zip_file_name = 'voyna-i-mir.txt.zip'
# zip_file = zipfile.ZipFile(zip_file_name, 'r')
# for filename in zip_file.namelist():
#     zip_file.extract(filename)
# '''раззиповали файл и вытащили в директорию, но кодировка не ютф8
# а cp1251'''

class Chatterer:

    analyze_count = 4

    def __init__(self,zip_file_name):
        self.zip_file_name = zip_file_name
        self.stat = {}

    def unzip(self):
        zfile = zipfile.ZipFile(self.zip_file_name, 'r')
        for filename in zfile.namelist():
            zfile.extract(filename)
        return filename
    def collect(self, file_name):

        sequence = ' ' * self.analyze_count

        with open(file_name, 'r', encoding='cp1251') as file:
            for line in file:
                line = line[:-1]
                # print(line)
                for char in line:
                    if sequence in self.stat:
                        if char in self.stat[sequence]:
                            self.stat[sequence][char] += 1
                        else:
                            self.stat[sequence][char] = 1
                    else:
                        self.stat[sequence] = {char: 1}
                    sequence = sequence[1:] + char
    def prepare(self):
        self.totals = {}
        self.stat_for_generate = {}

        for sequence, char_stat in self.stat.items():
            self.totals[sequence] = 0
            self.stat_for_generate[sequence] = []
            for char, count in char_stat.items():
                self.totals[sequence] += count
                self.stat_for_generate[sequence].append([count, char])
                self.stat_for_generate[sequence].sort(reverse=True)

    def chat(self, N):
        self.N = 1000
        printed = 0

        sequence = ' ' * self.analyze_count
        spaces_printed = 0
        while printed < N:
            char_stat = self.stat_for_generate[sequence]
            total = self.totals[sequence]
            dice = random.randint(1, total)
            pos = 0
            for count, char in char_stat:
                pos += count
                if dice <= pos:
                    break
            print(char, end='')
            if char == ' ':
                spaces_printed += 1
                if spaces_printed >= 10:
                    print()
                    spaces_printed = 0
            printed += 1
            sequence = sequence[1:] + char


chatterer = Chatterer(zip_file_name='voyna-i-mir.txt.zip')

file_name = chatterer.unzip()
chatterer.collect(file_name)
chatterer.prepare()
chatterer.chat(N=10000)



#
# file_name = 'voyna-i-mir.txt'
# stat = {}
# stat = {'a': {'т': 500, 'х': 5}, 'т': {'о': 100, 'у': 50}, }
#
# analyze_count = 4
#
# sequence = ' ' * analyze_count
#
# with open(file_name, 'r', encoding='cp1251') as file:
#      for line in file:
#          line = line[:-1]
#          # print(line)
#          for char in line:
#              if sequence in stat:
#                  if char in stat[sequence]:
#                      stat[sequence][char] += 1
#                  else:
#                      stat[sequence][char] = 1
#              else:
#                  stat[sequence] = {char: 1}
#              sequence = sequence[1:] + char
# #
# pprint(len(stat))

# totals = {}
# stat_for_generate = {}
#
# for sequence, char_stat in stat.items():
#     totals[sequence] = 0
#     stat_for_generate[sequence] = []
#     for char, count in char_stat.items():
#         totals[sequence] += count
#         stat_for_generate[sequence].append([count, char])
#     stat_for_generate[sequence].sort(reverse=True)

# N = 1000
# printed = 0
#
# sequence = ' ' * analyze_count
# spaces_printed = 0
# while printed < N:
#     char_stat = stat_for_generate[sequence]
#     total = totals[sequence]
#     dice = random.randint(1, total)
#     pos = 0
#     for count, char in char_stat:
#         pos += count
#         if dice <= pos:
#             break
#     print(char, end='')
#     if char == ' ':
#         spaces_printed += 1
#         if spaces_printed >= 10:
#             print()
#             spaces_printed = 0
#     printed += 1
#     sequence = sequence[1:] + char