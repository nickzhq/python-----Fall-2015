__author__ = 'Nick'

# coding=UTF-8

# Houqi Zuo
# Homework#04 -- Python

import pickle
import shelve

def process_data( name1 , name2 ):
	'''
	# This codes use pickle technique
	f = open( name1 ,'rb')
	try:
		data = pickle.load( f )
	finally:
		f.close()

	return data
	'''

	#This codes use shelve technique
	f = shelve.open( name2 )
	return f
