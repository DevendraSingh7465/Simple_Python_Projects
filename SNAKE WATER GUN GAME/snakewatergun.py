# snake > water
# water > gun
# gun > snake
import random
rules = '''
SNAKE WATER GUN GAME
RULES FOR THIS GAME...
  PRESS 1 FOR SNAKE
  PRESS 2 FOR WATER
  PRESS 3 FOR GUN
IF YOU WANT TO STOP THE GAME PRESS "0"
LET'S START WITH THE GAME...
'''
print(rules)
human_wins = 0
bot_wins = 0
draws = 0
total_chances = 0

while True:
    total_chances +=1
    human = int(input("ENTER YOUR CHOICE : "))
    if(human==0):
        total_chances -= 1
        break
    bot = random.randint(1,3) # both lower and upepr limit will be counted
    print("COMPUTER CHOICE :",bot)
    if(human==bot):
        print("DRAW")
        print()
        draws +=1
    elif(human==1 and bot==2):
        print("YOU WIN")
        print()
        human_wins+=1
    elif(human==1 and bot==3):
        print("BOT WINS")
        print()
        bot_wins +=1
    elif(human==2 and bot==1):
        print("BOT WINS")
        print()
        bot_wins +=1
    elif(human==2 and bot==3):
        print("YOU WIN")
        print()
        human_wins+=1
    elif(human==3 and bot==1):
        print("YOU WIN")
        print()
        human_wins+=1
    elif(human==3 and bot==2):
        print("BOT WINS")
        print()
        bot_wins +=1
    else:
        print("INVALID INPUT !")
        print()
        total_chances -= 1


print("TOTAL CHANCES PLAYED BY YOU :",total_chances)
print("COMPUTER WINS :",bot_wins)
print("YOUR WINS :",human_wins)
print("DRAWS :",draws)
if(human_wins>bot_wins):
    print("CONGRATULATIONS YOU WON...")