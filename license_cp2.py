iimport sys

print('LICENSE ISSUE CHECK')

def license_issue(age,hours):
	if age<16: print('License not issued.Age should be 16 or more')
	elif hours<200: print('License not issued. Practice hours should be 200 or more')
	else: print('Congratulations. License issued')

try:
	age=float(input('Enter your age:  '))
	hours=float(input('Enter practise hours:  '))
except:
	print('Invalid input.Enter numeric input only')
	sys.exit()

license_issue(age,hours)

