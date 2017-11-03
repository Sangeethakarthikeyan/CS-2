for i in range(1,51):   #for i = 1 to 50
	if(i%3==0 and i%5==0): print('fizzbuzz')		#check if i is a multiple of both 3 and 5
	elif i%3==0: print('fizz')						#check if i is a multiple of 3
	elif i%5==0: print('buzz')						#check if i is a multiple of 5
	else: print(i)									# print the number itself if it is not both multiple of 3 or 5
