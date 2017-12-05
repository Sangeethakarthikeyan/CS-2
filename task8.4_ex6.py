import sys

num_list=list()				# Empty list to which elements would be added
while True:
	num=input('Enter a number: ')
	if num=='done':break	# Break if input is done
	try: 
		f_num=float(num)	# Convert to float
	except:
		print('Enter numeric input only')
		sys.exit()
	num_list.append(f_num)	# Add the inputs as elements of list 

if len(num_list)!=0:		# If not first input is 'done', proceed. Otherwise print max and min cannot be found
	print('Maximum: ', max(num_list))
	print('Minimum: ', min(num_list))
else: print('Maximum and minimum cannot be found. It is an empty list')

