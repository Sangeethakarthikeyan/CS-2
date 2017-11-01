# initilaize all output variables
largest_so_far=None
smallest_so_far=None
total=0
count=0

while True:
	try: 
		number=input('Enter a number:  ')	#Getting input
		if(number)=='done': break			#stop getting input if input is 'done'
		number=int(number)

		#To update largest_so_far
		if (largest_so_far is None): largest_so_far=number
		elif (number>largest_so_far): largest_so_far=number

		#To update smallest_so_far
		if (smallest_so_far is None): smallest_so_far=number	
		elif (number<smallest_so_far): smallest_so_far=number

		#To update total and count
		total=total+number
		count=count+1

	except:
		print('Invalid input')
	
#print the final values of total, count,largest_so_far and smallest_so_far		 	
print("Total: {} Count={} Largest={} Smallest={}".format(total,count,largest_so_far,smallest_so_far))


