__author__ = 'Nick'

# coding=UTF-8

# Houqi Zuo
# Homework#04 -- Python

import sys
import os
mod_path = os.getcwd()
sys.path.append(mod_path)
import searcher
import indexer
from datetime import datetime

dt1 = datetime.now()
print("this program begins at ", dt1)
d = indexer.process_data("raw_data.pickle", "fortunes_shelve")
searcher.search(d)
dt2 = datetime.now()
print("this program ends at ", dt2)
print("the costing of time is " ,(dt2 - dt1) )