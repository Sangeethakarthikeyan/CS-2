print('TEMPERATURE CHECK')

import sys

# function definition to check for temperature conditions
def temperature_check(temp):
	if temp<20: print('Bring heavy jacket')
	elif temp>30: print("Don't bring jacket")
	else: print('Bring light jacket')

# Get temperature input from user
try: temp=float(input('Enter the value of temperature: '))
except:
	print('Enter a numeric input')
	sys.exit()


#Call temperature_check function after getting input
temperature_check(temp)


