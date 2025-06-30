import os 
import shutil
import numpy 

f = open('test.txt','w+')
f.write('This is a test file')
f.close()

os.getcwd()
print(os.getcwd())
os.listdir()
print(os.listdir())

shutil.move('test.txt','test1.txt')
print(os.listdir())

shutil.move('test1.txt','test.txt')
print(os.listdir())

shutil.move('test.txt','test1.txt')
print(os.listdir())

