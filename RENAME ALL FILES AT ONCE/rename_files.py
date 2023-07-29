# rename all files at once usign os module
import os

# path = "E:\demo folder\\"
path = input("Enter Path : ")
path = path+"\\"
path.replace('\\','/')
print(path)
files = os.listdir(path)
# print(files)
i = 0
def Rename():
    global i
    extention = input("Enter Extention Name (example -> .png) : ")
    for filename in files:
        new_name = path+str(i)+extention
        old_name= path + filename
        os.rename(old_name,new_name)
        i  += 1
Rename()
print(f"Total Files Found : {i}")
print("All Files Renamed")

