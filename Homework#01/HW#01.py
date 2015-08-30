__author__ = 'Nick'
# Houqi Zuo
# python CSCI 6651-01 
# 8/30/2015 -- HW#01
name = input("Hi, what's your name?")
print("Hello "+name+"! Let's play a game!")
print("Think of random number from 1 to 100, and I'll try to guess it!")
num, count, min, max = 50, 0 , 0, 100
state = True
while state:
    result = input("Is it " + str(num) +" ?(yes/no)" )
    count += 1
    if result == "yes" :
        print("Yeey! I got it in " + str(count) + " tries!")
        decision = input("Do you want to play one more?(yes/no)")
        if decision == "no" :
            state = False
        num, count, min, max = 50, 0 , 0, 100
    elif result == "no" :
        temp = input("Is it larger than " + str(num) + " ?(yes/no)")
        if temp == "yes" :
            min = num
        else :
            max = num
        num = round( ( min + max ) / 2 )
print("Bye Bye!")
