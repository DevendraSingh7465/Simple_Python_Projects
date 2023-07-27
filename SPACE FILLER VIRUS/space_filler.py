import os
import requests
import random
import shutil
from tqdm import tqdm
import time

Drive_Letter = input("Enter Drive Letter Except \"C\" : ").upper()
#print(Drive_Letter)
print("Searching For Wifi...")
print()
def create_fake_directories():
    create_dir = f"{Drive_Letter}:/iNTEL"
    if not os.path.exists(f"{Drive_Letter}:/iNTEL"):
        os.mkdir(create_dir)

    create_dir = f"{Drive_Letter}:/Java 20.0.1"
    if not os.path.exists(f"{Drive_Letter}:/Java 20.0.1"):
        os.mkdir(create_dir)

    create_dir = f"{Drive_Letter}:/Microsoft office 15"
    if not os.path.exists(f"{Drive_Letter}:/Microsoft office 15"):
        os.mkdir(create_dir)

    create_dir = f"{Drive_Letter}:/MY SQL"
    if not os.path.exists(f"{Drive_Letter}:/MY SQL"):
        os.mkdir(create_dir)

    # print("created")
    
def Random_File_Name_Generator():
    ran_num = random.randint(1,6)
    if(ran_num==1):
        file_extention = ".exe"
    elif(ran_num==2):
        file_extention = ".dat"
    elif(ran_num==3):
        file_extention = ".vbs"
    elif(ran_num==4):
        file_extention = ".log"
    elif(ran_num==5):
        file_extention = ".xml"
    elif(ran_num==6):
        file_extention = ".bat"
    all_characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&()_-+="
    file_start_char = ''.join(random.sample(all_characters, 3))
    file_end_char = ''.join(random.sample(all_characters, 4))
    random_file_name = (file_start_char+"Dev"+file_end_char+file_extention)
    return random_file_name

def file_download():
    os.chdir(f"{Drive_Letter}:/iNTEL/")
    random_file_name = Random_File_Name_Generator()
    url = "https://docs.oracle.com/cd/E11882_01/server.112/e40540.pdf"
    with open(random_file_name, "wb") as f:
        f.write(requests.get(url).content)
        # print(f"File Downloaded")
        f.close()

def copy_files(source,destination):
    files = os.listdir(source)
    for f in files:
        random_file_name = Random_File_Name_Generator()
        shutil.copyfile(source+f,destination+random_file_name)
    # print("Files Copied")


create_fake_directories()
print('\r 10% Completed',end='')


try:
    file_download()
    print('\r 37% Completed',end='')
    for i in range(1,8):
        source = f"{Drive_Letter}:/iNTEL/"
        destination = f"{Drive_Letter}:/iNTEL/"
        copy_files(source,destination)
    print('\r 50% Completed',end='')
except Exception as e:
    print("Path Not Found.")

try:
    source = f"{Drive_Letter}:/iNTEL/"
    destination = f"{Drive_Letter}:/Java 20.0.1/"
    copy_files(source,destination)
    print('\r 66% Completed',end='')
except Exception as e:
    print("Path Not Found.")

try:
    source = f"{Drive_Letter}:/iNTEL/"
    destination = f"{Drive_Letter}:/Microsoft office 15/"
    copy_files(source,destination)
    print('\r 82% Completed',end='')
except Exception as e:
    print("Path Not Found.")

try:
    source = f"{Drive_Letter}:/iNTEL/"
    destination = f"{Drive_Letter}:/MY SQL/"
    copy_files(source,destination)
    print('\r 99% Completed',end='')
except Exception as e:
    print("Path Not Found.")

finally:
    
    time.sleep(1)
    print('\r Exception (e) Error: No Data Found')
    print("Thank You For Using This Code.")
    print("This Window will close Automatically.")
    time.sleep(2)







