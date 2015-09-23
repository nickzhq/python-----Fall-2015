__author__ = 'Nick'

# Houqi Zuo
# Homework#03 -- program#01 -- Python
# Date: 09/19/2015

def bunnyEars2( number ):
    # if number is 0
    if (number == 0):
        return 0
    # if number is odd
    elif (number % 2 != 0 ):
        return ( 2 + bunnyEars2( number -1 ) )
    #if number is even
    else :
        return ( 3 + bunnyEars2( number -1 ) )

#----------------------------------------------
while( True ):
    num = int( input("Please enter an non-negative integer number( -1 is exit ):") )
    if( num == -1 ):
        print("Bye Bye")
        break
    if ( num >= 0 ):
        print("bunnyEars2(%d): %d" %(num, bunnyEars2(num) ) )
    else:
        print("Please enter an non-negative integer number and try again!")