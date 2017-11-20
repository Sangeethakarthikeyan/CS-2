# Function definition to check if monkey_trouble or not
def monkey_trouble(a,b):
	print('Monkey_trouble: ', a==b)     #If a=b we are in trouble and it prints True	

# Get inputs to know if monkey-a and b are smiling or not
a=input('Is monkey-a smiling? Enter Y if yes and N if no \n').upper()
# Check if the input is Y or N. If not print invalid input
if (a=='Y' or a=='N'):
	b=input('Is monkey-b smiling? Enter Y if yes and N if no \n').upper()
	if (b=='Y' or b=='N') : monkey_trouble(a,b)	# calling function monkey_trouble	
	else: print('Invalid input. Please enter Y or N')
else: print('Invalid input. Please enter Y or N')





