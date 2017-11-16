import sys

#fucnction definition: sum_double
def sum_double(a,b):

	# Check if equal or not
	if a==b: return 2*(a+b)
	else: return a+b

#get inputs
try:
	a=int(float(input('Enter first number: ')))
	b=int(float(input('Enter second number: ')))
except:
	print('Enter numeric input')
	sys.exit()	

#print ("sum_double(%d,%d): %d " %(a,b,sum_double(a,b)))
print("sum_double({},{}):{}".format(a,b,sum_double(a,b)))
