import sys

print('Sleep_in_check'.upper())

# Function definition to decide sleep_in or not
def sleep_in(weekday,vacation):
	weekday = weekday == 'y' #if user enters either 'Y' or 'y', variable weekday will be assigned True otherwise False.
	vacation =vacation == 'y'  #if user enters either 'Y' or 'y', variable vacation will be assigned True otherwise False.
	if vacation or not weekday: print("\nSleep in tight!")
	else: print("\nGo to Work!")

#Get input to know if it is a weekend, vacation
weekday=input('Is it a weekday? Enter Y if yes or N if no:  ').lower()


# Sleep_in Function call after getting inputs
if(weekday=='y' or weekday=='n'):
	vacation=input('Are we on a vacation? Enter Y if yes or N if no:  ').lower()
	if (vacation=='y' or vacation=='n'): sleep_in(weekday, vacation)
	else: 
		print('Invalid input. Enter either Y or N')
		sys.exit()
else:
	print('Invalid input. Enter either Y or N')
	sys.exit()

	

