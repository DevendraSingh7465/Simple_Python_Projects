# write a program to pronounce list of names using win32 API 
# Module Used win32com.client

import win32com.client

# Create an instance of the SAPI5 speech recognition engine
speaker = win32com.client.Dispatch("SAPI.SpVoice")

print("Type \"STOP\" to exit the loop.")
while 1:
    List = input("Write Text which you want to convert in speech : ").lower()
    if List == "stop":
        break
    else:
        speaker.Speak(List)



