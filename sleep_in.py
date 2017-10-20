import sys
# Get input to know if it is a weekday

weekday=input('Is it a weekday? Enter Y if yes and N if no \n')
if weekday=='Y': weekday='True'
elif weekday=='N': weekday='False'
else:
	print('Invalid input')
	sys.exit()

# Get input to know if vacation or not

vacation=input('Are we on a vacation? Enter Y if yes and N if no \n')
if vacation=='Y': vacation='True'
elif vacation=='N': vacation='False'
else:
	print('Invalid input')
	sys.exit()

# Check if sleep_in or not
if weekday=='False' or vacation=='True': print('True, we sleep in')
else: print('False, we dont sleep in')
