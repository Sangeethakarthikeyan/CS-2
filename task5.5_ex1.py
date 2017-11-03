#initialise all output variables
count=0
total=0

while True:
	try: 
		number=input('Enter a number:  ') 	# Get input
		if(number)=='done': break			#Stop getting input if input is 'done'		
		number=int(float(number))					
		#To update total and count
		total=total+number
		count=count+1

	except:
		print('Invalid input')
# Compute average (3methods to avoid ZeroDivisionError)

avg=(total/count) if count!=0 else 0

'''try: avg=(total/count)
except ZeroDivisionError:
	avg=0'''
	
'''if count==0: avg=0
else: avg=(total/count)'''

	
# print the final values of total, count, average												
print(total,count,avg)			




