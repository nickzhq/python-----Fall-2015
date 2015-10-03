__author__ = 'Nick'
# Houqi Zuo
# Homework#04 -- Python
import os
path_user = input("Please type the path:")
filename_user = input("Please type the file name:")

# rt = os.path.dirname(path_user)
for root, dirs, files in os.walk(os.path.abspath(path_user) ):
    if ( filename_user in files ):
        print( os.path.join( root, filename_user ) )
print("bye bye")
