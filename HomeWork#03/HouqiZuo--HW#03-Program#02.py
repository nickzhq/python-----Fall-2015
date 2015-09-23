__author__ = 'Nick'

mylist=["one", "two","eleven",  "one", "three", "two", "eleven", "three", "seven", "eleven"]

def count_frequency( mylist ):
    myset = set( mylist )
    mydict = { word:0 for word in myset }
    for word in mylist:
        mydict[word] += 1
    return mydict

print( count_frequency( mylist ) )
