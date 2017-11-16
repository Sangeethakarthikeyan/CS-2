import sys

print('LICENSE ISSUE CHECK')

def license_issue(age,hours):
	if age<16:
		if hours<200: print('License not issued.Age should be 16 or more and practice hours should be 200 or more')
		else: print('License not issued. Age should be 16 or more')
	elif hours<200: print('License not issued. Practice hours should be 200 or more')
	else: print('Congratulations. License issued')

try:
	age=float(input('Enter your age:  '))
	hours=float(input('Enter practise hours:  '))
except:
	print('Enter numeric input')
	sys.exit()

license_issue(age,hours)


