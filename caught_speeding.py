import sys

# Get inputs for speed
try:
	speed=int(input('Enter the speed:  '))
except:
	print('Enter a numeric input')
	sys.exit()

# Get inputs for is_birthday

is_birthday=input('Is today your birthday? Enter Y if yes and N if No:   ')

# checking if input is either Y/y or N/n
if(is_birthday=='Y' or is_birthday=='y' or is_birthday=='N' or is_birthday=='n'):
	
	is_birthday=(is_birthday=='Y' or is_birthday=='y') 	# is_birthday=True if input is Y/y
else: 
	print('Invalid input. Enter either Y or N')
	sys.exit()

# bonus speed limit=5 if birthday
if is_birthday: bonus=5
else: bonus=0

#assigning tickets based on speed limit and birthday bonus

if(speed<= 60+bonus): ticket=0
elif (speed<=80+bonus): ticket=1
else: ticket=2

# printing the output in the format of caught_speeding(speed,is_birthday):ticket-number
print("caught_speeding({},{}):{}".format(speed,is_birthday,ticket))
