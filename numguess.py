import sys
import random

correct=random.randint(1,9)			#fix the correct guess

while True:
	try: num=int(float(input('Guess a number between 1 to 9:   ')))
	except:		#prompt user for a numeric data and get the input again
		print('Wrong input. Enter numeric data only')
		continue
	if num>0 and num<=9:   	# check if input is between 1 to 9. Else prompt the user that it is wrong input and get input again
		if num==correct:	# if correct guess, say well guessed and exit . Otherwise get input again	
			print('Well guessed!')
			sys.exit()
		else: 
			print('Wrong guess.Try again')
			continue
	else:
		print('Wrong input. Numbers between 1 to 9 only allowed')
		continue
