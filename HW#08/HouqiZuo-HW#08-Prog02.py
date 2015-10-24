__author__ = 'Nick'

from random import randrange


print("INTEGER DIVISIONS")
while(True):
    a = randrange( 0, 5 )
    b = randrange( 0,10 ) * a
    try:
        result = input("%i / %i = "%(b, a) )
        if(  int(result) == b/a ):
            print("CORRECT!")
        else:
            print("INCORRECT!")
    except ValueError:
        print("Please enter Integers Only!")
    except Exception as e:
        print("INCORRECT!")

