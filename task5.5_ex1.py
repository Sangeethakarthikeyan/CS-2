#initialise all output variables
count=0
total=0

while True:
	try: 
		number=input('Enter a number:  ') 	# Get input
		if(number)=='done': break			#Stop getting input if input is 'done'		
		number=int(number)					
		#To update total and count
		total=total+number
		count=count+1
	except:
		print('Invalid input')
	
avg=total/count								# Compute average
print(total,count,avg)						# print the final values of total, count, average


