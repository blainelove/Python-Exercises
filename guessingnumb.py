import logging
import random


def guessing():
	right = random.randrange(1,11)
	logging.info(right)

	guess = int(input('Enter number 1-10: ')) #prompt user to enter a number

	#keep prompting user to enter a new guess until the right number is guessed
	while guess != right:
		guess = int(input('Try Again:'))
	
	return "Correct!"


print (guessing())
