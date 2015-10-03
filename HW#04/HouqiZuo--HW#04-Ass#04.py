__author__ = 'Nick'
# Houqi Zuo
# Homework#04 -- Python
import pickle
import shelve
import os

# this is the format for pickle store and pickle read
#data = ()
# store the data using pickle
def pickle_store( name, age, country):

    data = pickle_read()
    temp = ( name, age, country )
    data = list( data )
    data.append(temp)
    data = tuple( data )

    f = open("store_pickle.txt",'wb')
    try:
        pickle.dump( data, f )
    finally:
        f.close()

# read from pickle_store
def pickle_read():
    #global data
    if (os.path.exists( "store_pickle.txt") ):
        f = open("store_pickle.txt",'rb')
        data = pickle.load( f )
        f.close()
    else:
        data = ()
    return data

# store the data using shelve
def shelve_store( name, age, country ):
    f = shelve.open("store_shelve", writeback=True)
    i = f.__len__()
    try:
        f[ str(i+1) ] = ( name,age, country )
    finally:
        f.close()

# read the data using shelve
def shelve_read():
    f = shelve.open("store_shelve")
    return f

name = input("Enter a name:")
age = input("Enter the age:")
country = input("Enter the country:")

pickle_store( name, age, country )
data = pickle_read()
print("Read data from pickle text")
for item in data:
    print( "Information: ", item  )

shelve_store( name, age, country )
print("Read data from shelve")
data_shel = shelve_read()
for i in data_shel.values():
    print("Information: ", i )
print("Bye Bye")



