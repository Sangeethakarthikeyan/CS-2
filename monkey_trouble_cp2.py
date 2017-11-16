# Function definition to check if monkey_trouble or not
def monkey_trouble(a,b):
	# Check if the input is Y or N. If not print invalid input
	if (a=='Y' or a=='N') and (b=='Y' or b=='N') :
		print('Monkey_trouble: ', a==b)     #If a=b we are in trouble and it prints True
	else: print('Invalid input. Please enter Y or N')

# Get inputs to know if monkey-a and b are smiling or not
a=input('Is monkey-a smiling? Enter Y if yes and N if no \n').upper()
b=input('Is monkey-b smiling? Enter Y if yes and N if no \n').upper()

# calling function monkey_trouble
monkey_trouble(a,b)

