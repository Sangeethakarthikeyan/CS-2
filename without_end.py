#function definition of without_end
def without_end(a):
	return a[1:len(a)-1]

# Getting a string as user input
a=input('Enter a string:')
print('output: ', without_end(a))  # Function call in the print statement

