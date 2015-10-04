__author__ = 'Nick'

# coding=UTF-8

# Houqi Zuo
# Homework#04 -- Python
import os
from datetime import datetime

def search( data_list ):
	# get input from user
	query= input("query:")
	# split the string
	query = query.split()
	# delete the duplicated element
	search=set(query)
	# delete "and" and "or"
	# when boolOperator is 1. perform "and" operator
	# when boolOperator is 0. perform "or" operator
	boolOperator = 1
	if ( "and" in search ):
		search.remove("and")
	if ( "or" in search ):
		search.remove("or")
		boolOperator = 0
	# print
	if (boolOperator):
		print("Performing AND search for:", search )
	else:
		print("Performing OR search for:", search )

	mydict = { word:None for word in search }

	# get current time
	dt1 = datetime.now()
	print( "The time before search ; ", dt1)
	#start_time = time.monotonic()*10000

	'''
	# This codes use pickle technique
	# perform search
	# AND perform
	if (boolOperator):
		# search
		for tuple_in_list in data_list:
			#print(type(tuple_in_list))
			mydict = { x:None for x in mydict.keys() }
			for key in mydict.keys():
				if( key in tuple_in_list[1] ):
					mydict[key] = 1
			# output
			if ( None not in mydict.values() ):
				# get current time
				print("Found at:", tuple_in_list[0] )
				print("The last modified time: ", os.path.getmtime( tuple_in_list[0] ) )
				print("The size of file is: ", os.path.getsize( tuple_in_list[0] ) )
				break
	# OR perform
	else:
		# search one line by one line
		for tuple_in_list in data_list:
			# search
			for key in mydict.keys():
				if ( key in tuple_in_list[1] ):
					# get current time
					print("Found at:" ,tuple_in_list[0])
					print("The last modified time: ", os.path.getmtime( tuple_in_list[0] ) )
					print("The size of file is: ", os.path.getsize( tuple_in_list[0] ) )
					break
	'''
	# This codes use shelve technique
	# perform search
	# AND perform
	if (boolOperator):
		# search
		for i,dict_shelve in data_list.items():
			#print(type(tuple_in_list))
			word = dict_shelve.split()
			mydict = { x:None for x in mydict.keys() }
			for key in mydict.keys():
				if( key in word ):
					mydict[key] = 1
			# output
			if ( None not in mydict.values() ):
				# get current time
				print("Found at:", i )
				print("The last modified time: ", os.path.getmtime( i ) )
				print("The size of file is: ", os.path.getsize( i ) )
	# OR perform
	else:
		# search one line by one line
		for i,dict_shelve in data_list.items():
			word = dict_shelve.split()
			# search
			for key in mydict.keys():
				if ( key in word ):
					print("Found at:" ,i)
					print("The last modified time: ", os.path.getmtime( i ) )
					print("The size of file is: ", os.path.getsize( i ) )
					break
	#end_time = time.monotonic() *10000.
	dt2 = datetime.now()
	print( "The time after search : ", dt2)
	print( "Execution time: %d ms" % (dt2.microsecond - dt1.microsecond) )