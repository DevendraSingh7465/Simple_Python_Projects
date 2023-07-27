# write a pyhton program to translate a simple english word into secret code langauge 

def Encoding_Message():
    import random
    all_characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!#$%^&*(){}[]|<>?/"
    random_character1= ''.join(random.sample(all_characters, 2))
    random_character2= ''.join(random.sample(all_characters, 2))
    i = 0
    
    for i in range(len(final_msg_in_list)):
        change = final_msg_in_list[i]
        if(len(change)==1):
            #leave as it is
            encoded_msg.append(change)
        elif(len(change)==2):
            #just reverse
            encoded_msg.append(change[-1: :-1])
            
        elif(len(change)==3):
            # last word in front
            addinfront = change[-1]
            concate_infront = (addinfront+change)
            final_word = concate_infront[:-1]
            encoded_msg.append(final_word)

        elif(len(change)==4):
            #first word in last 
            addinlast = change[0]
            concate_inlast = (change+addinlast)
            final_word = concate_inlast[1:]
            encoded_msg.append(final_word)

        elif(len(change)>4):
            # first word in last 
            # add random string character in starting and ending
            addinlast = change[0]
            concate_inlast = (change+addinlast)
            without_random_word = concate_inlast[1:]
            with_random_word = (random_character1+without_random_word+random_character2)
            encoded_msg.append(with_random_word)
        else:
            print("Invalid Message")
            break
    
def Decoding_Message():
    i = 0
    for i in range(len(final_msg_in_list)):
        change = final_msg_in_list[i]
        if(len(change)==1):
            #leave as it is
            decoded_msg.append(change)
        elif(len(change)==2):
            #just reverse
            decoded_msg.append(change[-1: :-1])
            
        elif(len(change)==3):
            #first word in last 
            addinlast = change[0]
            concate_inlast = (change+addinlast)
            final_word = concate_inlast[1:]
            decoded_msg.append(final_word)

        elif(len(change)==4):
            # last word in front
            addinfront = change[-1]
            concate_infront = (addinfront+change)
            final_word = concate_infront[:-1]
            decoded_msg.append(final_word)

        elif(len(change)>4):
            # remove 2 random string character in starting and ending
            # last word in first 
            remove_front1 = change[1:]
            remove_front2 = remove_front1[1:]
            remove_last1 = remove_front2[:-1]
            remove_last2 = remove_last1[:-1]
            
            addinfront = remove_last2[-1]
            concate_infront = (addinfront+remove_last2)
            final_word = concate_infront[:-1]
            decoded_msg.append(final_word)
            #decoded_msg.append()
        else:
            print("Invalid Message")
            break

intro_msg = '''
THIS PROGRAM ENCODES AND DECODES SECRETE CODE
PRESS 1 FOR ENCODING 
PRESS 2 FOR DECODING
'''
print(intro_msg)
intro_choice = int(input("ENTER YOUR CHOICE : "))


if(intro_choice==1):
    encoding_msg = '''
ENCODING...
PRESS 1 TO UPLOAD TXT FILE AND ENCODE THE DATA INSIDE FILE
PRESS 2 TO WRITE YOUR MESSAGE AND ENCODE
    '''
    print(encoding_msg)
    encoding_msg_choice = int(input("ENTER YOUR CHOICE : "))


    if(encoding_msg_choice==1):
        file_path = input("PLEASE PASTE YOUR FILE PATH : ") 
        #E:\All Programs\Python Codes (in VS)\Python Projects\Secret Codeing
        file_name = input("ENTER YOUR FILE NAME(without extention) : ")
        #demo
        full_file_name = file_path+"\\"+(file_name+".txt") 

        f = open(full_file_name,"r")
        #print(f.read())
        msg_in_list = []
        for line in f:
            line_strip = line.strip()
            line_split = line_strip.split()
            msg_in_list.append(line_split)

        #print(msg_in_list)
        final_msg_in_list = []
        for i in msg_in_list:
            for j in i:
                final_msg_in_list.append(j)

        #print(final_msg_in_list)

        encoded_msg = []
        Encoding_Message()

        #print(encoded_msg)
        new_file = file_path+"\\"+(file_name+"_ENCODED.txt") 
        f1 = open(new_file,"w")
        new_file_name = file_name+"_ENCODED.TXT"
        for i in range(len(encoded_msg)):
            encoded_message = encoded_msg[i]+" "
            f1.write(encoded_message)
        print("NEW FILE CREATED SUCCESSFULLY WITH ENCODED MESSAGE IN SAME DIRECTORY.")
        print("NEW FILE NAME :",new_file_name)
        f.close()
        f1.close()
    elif(encoding_msg_choice==2):
        content = input("ENTER YOUR MESSAGE WHICH YOU WANT TO ENCODE : ").lower()
        final_msg_in_list = content.split()

        encoded_msg = []
        Encoding_Message()
        encoded_lst_in_string = ' '.join(encoded_msg)
        print("ENCODED MESSAGE :",encoded_lst_in_string)
    else:
        print("INVALID CHOICE !")
        

elif(intro_choice==2):
    decoding_msg = '''
DECODING...
PRESS 1 TO UPLOAD TXT FILE AND DECODE THE DATA INSIDE FILE
PRESS 2 TO WRITE YOUR MESSAGE AND DECODE
    '''
    print(decoding_msg)
    decoding_msg_choice = int(input("ENTER YOUR CHOICE : "))


    if(decoding_msg_choice==1):
        file_path = input("PLEASE PASTE YOUR FILE PATH : ") 
        #E:\All Programs\Python Codes (in VS)\Python Projects\Secret Codeing
        file_name = input("ENTER YOUR FILE NAME(without extention) : ")
        #demo
        full_file_name = file_path+"\\"+(file_name+".txt") 

        f = open(full_file_name,"r")
        #print(f.read())
        msg_in_list = []
        for line in f:
            line_strip = line.strip()
            line_split = line_strip.split()
            msg_in_list.append(line_split)

        #print(msg_in_list)
        final_msg_in_list = []
        for i in msg_in_list:
            for j in i:
                final_msg_in_list.append(j)

        #print(final_msg_in_list)

        decoded_msg = []
        Decoding_Message()

        #print(decoded_msg)
        new_file = file_path+"\\"+(file_name+"_ENCODED.txt") 
        f1 = open(new_file,"w")
        new_file_name = file_name+"_DECODED.TXT"
        for i in range(len(decoded_msg)):
            decoded_message = decoded_msg[i]+" "
            f1.write(decoded_message)
        print("NEW FILE CREATED SUCCESSFULLY WITH ENCODED MESSAGE IN SAME DIRECTORY.")
        print("NEW FILE NAME :",new_file_name)
        f.close()
        f1.close()
    elif(decoding_msg_choice==2):
        content = input("ENTER YOUR MESSAGE WHICH YOU WANT TO DECODE : ").lower()
        final_msg_in_list = content.split()
        decoded_msg = []
        Decoding_Message()
        decoded_lst_in_string = ' '.join(decoded_msg)
        print("ENCODED MESSAGE :",decoded_lst_in_string)
    else:
        print("INVALID CHOICE !")


else:
    print("INVALID CHOICE !")
    