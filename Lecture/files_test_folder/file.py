# Варианты режима (мод):
# a – открытие для добавления данных.
# ○ Позволяет дописывать что-то в имеющийся файл.
# ○ Если вы попробуете дописать что-то в несуществующий файл, то файл будет создан
# и в него начнется запись.
# r – открытие для чтения данных.
# ○ Позволяет читать данные из файла.
# ○ Если вы попробуете считать данные из файла, которого не существует, программа
# выдаст ошибку.
# w – открытие для записи данных.
# ○ Позволяет записывать данные и создавать файл, если его не существует.
#
# 1. w+
# ○ Позволяет открывать файл для записи и читать из него.
# ○ Если файла не существует, он будет создан.
# 2. r+
# ○ Позволяет открывать файл для чтения и дописывать в него.
# ○ Если файла не существует, программа выдаст ошибку.

color = ["red", '8885', 'blue']
data = open('file.txt','a') # а - режим работы
data.writelines(color)
data.close()

with open('file.txt', 'w') as data:
    data.write('line 1\n')
    data.write('line 2\n')
    data.writelines("line 3\n")
    data.writelines("line 4")

path="file.txt"
data = open(path,'r')
for line in data:
    print(line)
data.close()

import os

# read from file


print(os.getcwd()) # P:\IT\PythonСourseGB\Lecture\files_test_folder
print("\n")
print(os.path.basename('P:/IT/PythonСourseGB/Lecture/files_test_folder/file.txt')) # file.txt
print("\n")
print(os.path.abspath('file.txt')) # P:\IT\PythonСourseGB\Lecture\files_test_folder\file.txt
print("\n")

import shutil as sh
sh.copyfile('file.txt','file_2.txt')



