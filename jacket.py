print('Temperature check')

import sys

# Get temperature input from user
try: temp=float(input('Enter the value of temperature: '))
except:
	print('Enter a numeric input')
	sys.exit()

# check for temperature conditions
if temp<20: print('Bring heavy jacket')
elif temp>30: print("Don't bring jacket")
else: print('Bring light jacket')
