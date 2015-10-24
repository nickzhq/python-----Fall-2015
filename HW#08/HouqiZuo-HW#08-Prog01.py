# define the Animal class
class Animal:
	dict ={'elephant': ("I have exceptional memory!", "I have a long noise!", "I am the largest land-living mammal in the world!"),
		   'tiger': ("I am the biggest cat!", "I come in black and white or orange and black!", "I am a carnivores!"),
		   'bat':("I use echo-location!", "I can fly!", "I see well in dark!") }
	# initialize the variable
	def __init__(self, name):
		self.name = name
	# guess who I am
	def guess_who_I_am(self):
		print("\nI will give you 3 hints, guess what animal I am\n")
		for hints in Animal.dict[self.name]:
			print(hints)
			guess_name = input("Who am I!?: ")
			if ( guess_name == self.name ):
				print( "You got it! I am ", self.name )
				break
			else:
				print("Nope, try again!")
			if ( hints == Animal.dict[self.name][-1]):
				print("\nI'm out of hints! The answer is: ", self.name)

e = Animal("elephant")
t = Animal("tiger")
b = Animal("bat")

e.guess_who_I_am()
t.guess_who_I_am()
b.guess_who_I_am()

print("Bye Bye")



		