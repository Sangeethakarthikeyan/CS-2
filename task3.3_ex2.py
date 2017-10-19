try:
	hours=input('Enter hours: ')
	h=float(hours)
	rate=input('Enter rate: ')
	r=float(rate)
	if h<=40:
		pay=h*r	
	else:
		pay=(40*r)+(h-40)*1.5*r
	print('Pay:',pay)
except:
	print('Error, please enter a numeric input')
