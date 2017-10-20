print('License issue check')

import sys

# Get user input for age and practise hours
try:
	age=float(input('Enter your age: '))
	hours=float(input('Enter practice hours: '))
except:
	print('Please enter numeric input')
	sys.exit()

#checking for age and practise hours
if age<16: print('Sorry, License cannot be issued')
else:	
	if hours<=200: print('Sorry,License cannot be issued')
	else: print('Congratulations. License issued') 


