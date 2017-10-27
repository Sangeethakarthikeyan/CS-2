import sys

# function definition: To compute the pay
def computepay(hours,rate):
	if hours<=40: pay=hours*rate
	else: pay=(40*rate)+(hours-40)*1.5*rate
	#print the output:pay
	print('Pay:',pay)

#actual program
# Get the inputs hours and rate
try:
	hours=float(input('Enter hours:'))
	rate=float(input('Enter rate:'))
except:
	print('Error, please enter numeric input')
	sys.exit()
#computepay function call
computepay(hours,rate)
