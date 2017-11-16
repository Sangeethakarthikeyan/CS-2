import sys

#Function definition for caught_speeding
def caught_speeding(speed,is_birthday):	

	# bonus speed limit=5 if birthday
	if is_birthday: bonus=5
	else: bonus=0

	#assigning tickets based on speed limit and birthday bonus

	if(speed<= 60+bonus): return 0
	elif (speed<=80+bonus): return 1
	else: return 2

# Get inputs for speed
try:
	speed=int(float(input('Enter the speed:  ')))
except:
	print('Enter a numeric input')
	sys.exit()
# Get inputs for is_birthday
is_birthday=input('Is today your birthday? Enter Y if yes and N if No:   ').upper()

# checking if input is either Y/y or N/n
if(is_birthday=='Y' or is_birthday=='N'):
	is_birthday=is_birthday=='Y' 	# is_birthday=True if input is Y/y
	# printing the output in the format of caught_speeding(speed,is_birthday):ticket-number
	print("caught_speeding({},{}):{}".format(speed,is_birthday,caught_speeding(speed, is_birthday))) # Function call inside print function
else: 
	print('Invalid input. Enter either Y or N')
	sys.exit()


	

