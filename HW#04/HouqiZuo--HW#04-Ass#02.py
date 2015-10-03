__author__ = 'Nick'
# Houqi Zuo
# Homework#04 -- Python
import os

filename_user = input("Please enter the file name:")
if( os.path.isfile( filename_user ) ):
    file_in = open( filename_user )
    try:
        for i,line in enumerate(file_in):
             if ("password=" in line ):
                 print("Found the password in line {0}: {1}".format(i + 1, line) )
    finally:
        file_in.close()
    print("Bye Bye")
else:
    print("This is NOT a valid filename!")