# Function definition of chop. Doesnt return anything. Argument unmodified
def chop(t):
	t=t[1:(len(t)-1)]

# Function definition of middle. Returns a new list. Argument unmodified
def middle(t):
	return t[1:len(t)-1]

num_list=[1,2,3,4,5]
print('output of chop: ', chop(num_list))  	
print('output of middle: ', middle(num_list))
print('Original list: ', num_list)
