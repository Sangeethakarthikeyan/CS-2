# Get input to know if it is a weekday
weekday=input('Is it a weekday? Enter Y if yes and N if no \n')
vacation=input('Are we on a vacation? Enter Y if yes and N if no \n')


# Decide if sleep in or not
if (weekday=='Y' or weekday=='N') and (vacation=='Y' or vacation=='N'): 
	print('sleep in : ', weekday=='N' or vacation=='Y' )
else: 
	print('Invalid input. Please enter Y or N')
