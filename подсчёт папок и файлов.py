import os
print("Скрипт считает папки и графические файлы")
d=input("Введите каталог, где нужно подсчитать папки и графические файлы: ")
dd=0
ff=0

print(os.walk(d))

for dirpath, dirnames, filenames in os.walk(d):
    # перебрать каталоги
    for dirname in dirnames:
        print("Каталог:", os.path.join(dirpath, dirname))
        dd+=1
    # перебрать файлы
    for filename in filenames:
    	if "jpg" in filename or "png" in filename or "jpeg" in filename or "JPG" in filename:
	        print("Файл:", os.path.join(dirpath, filename), ff)
	        ff+=1

print("папок: ",dd)
print("файлов: ",ff)

input()