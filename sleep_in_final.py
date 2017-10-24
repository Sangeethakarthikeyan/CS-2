import sys

# Get input to know if it is a weekend, vacation
weekday=input('Is it a weekend? Enter Y if yes or N if no:  ')
vacation=input('Are we on a vacation? Enter Y if yes or N if no:  ')

if (weekday=='Y' or weekday=='y' or weekday=='N' or weekday=='n') and (vacation=='Y' or vacation=='y' or vacation=='n' or vacation=='N'):
	weekday=(weekday=='y' or weekday=='Y')
	vacation=(vacation=='y' or vacation=='Y')
else:
	print('Invalid input. Enter either Y or N')
	sys.exit()

#Decide if sleep_in or not based on vacation and weekday
if vacation or not weekday: sleep_in=True
else: sleep_in=False

#print output in the format of sleep_in(weekday,vacation):sleep_in
print("sleep_in({},{}):{}".format(weekday,vacation,sleep_in))
