'''
import os

f =os.listdir("dir")
print(f)

print(os.getcwd())

print(os.path.exists("harry"))

os.remove("sample.txt")
os.rmdir("dir")

'''

import shutil

shutil.rmtree("dir")
shutil.copy("harry.txt" , "john.txt")
