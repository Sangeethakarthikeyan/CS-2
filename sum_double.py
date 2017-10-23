import sys

#get inputs
try:
	a=int(input('Enter first number: '))
	b=int(input('Enter second number: '))
except:
	print('Enter numeric input')
	sys.exit()

# Check if equal or not
if a==b: 
	c=2*(a+b)
	#print ("sum_double(%d,%d): %d " %(a,b,c))
	print("sum_double({},{}):{}".format(a,b,c))
else: print("sum_double({},{}):{}".format(a,b,(a+b))) 
