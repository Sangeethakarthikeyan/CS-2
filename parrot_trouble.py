import sys

# Get input to know if parrot talking
talking=input('Is parrot talking? Enter Y if yes or N if no\n')

# To check if input is valid (either Y/N), else print invalid input
if talking=='Y' or talking=='y'or talking=='N' or talking=='n':
	
	talking=(talking=='Y' or talking=='y') # If input is y, talking=true

	# Getting hour input
	try:
		hour=int(input('Enter the value of hour: '))
	except:
		print('Enter numeric data')
		sys.exit()

	if hour<0 or hour>23: 	# checking if hour is within 0 to 23
		print('Enter a number between 0 to 23')
		sys.exit()
	elif (talking and (hour<7 or hour>20)): trouble=True # trouble=True if (hour<7 or hour>20) and talking=True
	else: trouble=False

	print("parrot_trouble({},{}):{}".format(talking,hour,trouble))

else:
	print('Invalid input. Enter Y or N')
