import time 

# time.strftime('%H:%M:%S'') is used to print time
timestamp = time.strftime('%H:%M:%S')
print("Current Time : ",timestamp)
hours = int(time.strftime('%H'))
if((hours>4) and (hours<12)):
    print("Good Morning...")
elif((hours>11) and (hours<18)):
    print("Good Afternoon...")
elif((hours>17) and (hours<20)):
    print("Good Evening...")
else:
    print("Good Night")


# time.time() check how much time it takes to run program
def UsingForLoop():
    for i in range(50):
        print(i)
def UsingWhileLoop():
    i=1
    while i < 51:
        print(i)
        i = i+1

calculate_Time = time.time()
UsingWhileLoop()
print(time.time()-calculate_Time)

calculate_Time = time.time()
UsingForLoop()
print(time.time()-calculate_Time)

# time.sleep("Enter Seconds to delay") will pause the execution of code by specified seconds
print("Hello")
time.sleep(2)
print("This is printed after 2 Seconds")
