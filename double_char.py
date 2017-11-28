#function definition of double_char
def double_char(a):
	b=''
	for i in range(0,len(a)):  # for first to last character
		b=b+a[i]+a[i]
	return b

# Getting a string as user input
a=input('Enter a string:')
print('output: ', double_char(a))  # Function call in the print statement

