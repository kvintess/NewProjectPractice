# -*- coding utf-8 -*-

import zipfile

zip_file_name = 'voyna-i-mir.txt.zip'
zip_file = zipfile.ZipFile(zip_file_name, 'r')
zip_file.printdir()