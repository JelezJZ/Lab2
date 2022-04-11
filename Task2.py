import hashlib
import os
from re import S
files_dict = {}
files = os.listdir('Task2')
for file in files:
    temp_file = open('./Task2/' + file)
    hash = hashlib.md5(temp_file.read().encode('utf-8')).hexdigest()
    if hash in files_dict:
        files_dict[hash].append(file)
    else:
        files_dict[hash] = [file]
    temp_file.close()
print(files_dict)