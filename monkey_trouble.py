# Get inputs to know if monkey-a and b are smiling or not
a=input('Is monkey-a smiling? Enter Y if yes and N if no \n')
b=input('Is monkey-b smiling? Enter Y if yes and N if no \n')

# Check if the input is Y or N. If not print invalid input
if (a=='Y' or a=='N') and (b=='Y' or b=='N') :
	print('Monkey_trouble: ', a==b)     #If a=b we are in trouble and it prints True
else: print('Invalid input. Please enter Y or N')

