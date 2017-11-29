def double_char(a):
                b=''
                for i in a:                                #note that with ‘in’ operator, for loop will traverse through each character of the string without using the range()
                    b+=i*2                #using ‘*’ operator, we can get so many multiple of the character.
                return b
 
# Getting a string as user input
a=input('Enter a string:')
print('output: ', double_char(a))  # Function call in the print statement
