import sys
 
 # Get input for day
try:
 	day=int(input('What day is today? Enter a number between 0 to 6.|Sunday:0|Monday:1|Tuesday:2|Wednesday:3|Thursday:4|Friday:5|Saturday:6|    '))
except:
 	print('Inalid input.Enter numeric data')
 	sys.exit()
 
#Check if day input is within range otherwise prompt a message and exit
if (day<0 or day>6): 
 	print('Invalid input.Enter a number between 0 to 6')
 	sys.exit()

# Get an input to know if vacation or not
vacation=input('Are we on a vacation? Enter Y if yes and N if no:   ')

# check if vacation input is valid (Y/N or y/n)
if(vacation=='Y' or vacation=='y' or vacation=='N' or vacation=='n'):
	vacation=(vacation=='Y' or vacation=='y')      # vacation=True if input is Y/y
else:
	print('Invalid input. Enter either Y or N')
	sys.exit()

weekend=(day==0 or day==6)                          # weekend=True if day= 0 or 6                

#Setting time based on vacation and weekend
if vacation:
	if weekend: time='off'
	else: time='10:00'
elif weekend: time='10:00'
else: time='7:00'

#print the output in the format of alarm_clock(day,vacation):time_as_string
print("alarm_clock({},{}):{}".format(day,vacation,time))
