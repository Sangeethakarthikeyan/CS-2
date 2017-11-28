#function definition of make_abba
def make_abba(a,b):
	return a+b+b+a

# Getting two strings as user input
a=input('Enter string a:')
b=input('Enter string b:')
print('output: ',make_abba(a,b)) # Function call in the print statement

