import time 
timestamp = time.strftime('%H:%M:%S')
print("Current Time : ",timestamp)


name = input("Enter Your Name : ")
print("Hello",name,",Get ready to play this Game.")

print("Let's Start with the game.")
print()
input("Press any key to continue.")
score = 0



Ques_1 = '''
Question 1 - India is the world's ____________ largest country by land area.
A. fifth
B. Sixth
C. Seventh 
'''
print(Ques_1)#C
ans_1 = input("Enter Your Option : ").casefold()
if(ans_1=="c"):
    score = score + 1

input("Press any key to continue.")
Ques_2 = '''
Question 2 - The Indian flag has three horizontal stripes of saffron (orange), white, and green with a ____ chakra (wheel) in the center.
A. Violet 
B. Blue
C. Indigo
'''
print(Ques_2)#B
ans_2 = input("Enter Your Option : ").casefold()
if(ans_2=="b"):
    score = score + 1
input("Press any key to continue.")
Ques_3 = '''
Question 3 - Which of these is the national animal of India ?
A. Peacock
B. Bengal Tiger
C. Lion
'''
print(Ques_3)#B
ans_3 = input("Enter Your Option : ").casefold()
if(ans_3=="b"):
    score = score + 1

print("Your Total Score is",score,"out of 3.")


