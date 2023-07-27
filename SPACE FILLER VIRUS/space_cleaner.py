import os
from tqdm import tqdm
import time

# add password
# find Dev keyword in the file name
password = input("Enter Password To remove Corrupted Files : ")

if(password=="dev@singh7465"):
    Drive_Letter = input("Enter Drive Letter : ").upper()
    # print(Drive_Letter)
    # total files found
    Total_Files_Searched = 0
    # corrupted files found
    Corrupted_Files_Found = 0
    

    def search_files(directory):
        global Total_Files_Searched
        global Corrupted_Files_Found
        total_files_found = os.listdir(directory)
        # print(f"Total Files in {directory} : {len(total_files_found)}")
        keyword = "Dev"
        matches = []
        for root, dirs, files in os.walk(directory):
            for file in files:
                if keyword in file:  
                    matches.append(os.path.join(root, file))
        # print("Corrupted Files Found :",len(matches))
        Total_Files_Searched += len(total_files_found)
        Corrupted_Files_Found += len(matches)
        for file in matches:
            os.remove(file)  
        # print("Corrupted Files Removed :",len(matches))
        

    try:
        directory = f"{Drive_Letter}:/inteL/"
        search_files(directory)
    except Exception as e:
        print("Path Not Found.")

    try:
        directory = f"{Drive_Letter}:/Java 20.0.1/"
        search_files(directory)
    except Exception as e:
        print("Path Not Found.")

    try:
        directory = f"{Drive_Letter}:/Microsoft office 15/"
        search_files(directory)
    except Exception as e:
        print("Path Not Found.")

    try:
        directory = f"{Drive_Letter}:/MY SQL/"
        search_files(directory)
    except Exception as e:
        print("Path Not Found.")

    finally:
        for i in tqdm(range(100)):
            time.sleep(0.01)
        print(f"Total Files Searched : {Total_Files_Searched}")
        print(f"Corrupted Files Found : {Corrupted_Files_Found}")
        print(f"Corrupted Files Removed : {Corrupted_Files_Found}")
else:
    print("Wrong Password.")
