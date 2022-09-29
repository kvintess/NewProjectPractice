# -*- coding utf-8 -*-

import zipfile

zip_file_name = 'voyna-i-mir.txt.zip'
zip_file = zipfile.ZipFile(zip_file_name, 'r')
for filename in zip_file.namelist():
    zip_file.extract(filename)
'''раззиповали файл и вытащили в директорию, но кодировка не ютф8'''
