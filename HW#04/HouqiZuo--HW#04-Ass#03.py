__author__ = 'Nick'
# Houqi Zuo
# Homework#04 -- Python

import shelve
from datetime import datetime
# for dictionary
dict = {}
dict["keyOne"] = []
dict["keyTwo"] = []
dict["keyThree"] = []
# test data on dictionary
dt1 = datetime.now()
for i in range(1000):
    dict["keyOne"].append(i)
    dict["keyTwo"].append(i)
    dict["keyThree"].append(i)
dt2 = datetime.now()

print("These operations on dictionary need %d ms" % ( dt2.microsecond - dt1.microsecond ) )

# for shelve
f = shelve.open("Ass#03-HW#04")
f["keyOne"] = []
f["keyTwo"] = []
f["keyThree"] = []
# test data on shelve
dt1 = datetime.now()
for i in range(1000):
    f["keyOne"].append(i)
    f["keyTwo"].append(i)
    f["keyThree"].append(i)
dt2 = datetime.now()

print("These operations on shelve need %d ms" % ( dt2.microsecond - dt1.microsecond ) )