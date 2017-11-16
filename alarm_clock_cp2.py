import sys

#Function definition:alarm_clock
def alarm_clock(day,vacation):
	weekend=(day==0 or day==6)                          # weekend=True if day= 0 or 6                
	
	#Setting time based on vacation and weekend
	if vacation:
		if weekend: return 'off'
		else: return '10:00'
	elif weekend: return '10:00'
	else: return '7:00'

 
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
vacation=input('Are we on a vacation? Enter Y if yes and N if no:   ').upper()

# check if vacation input is valid (Y/N or y/n)
if(vacation=='Y' or vacation=='N'):
	vacation=vacation=='Y'      # vacation=True if input is Y/y
else:
	print('Invalid input. Enter either Y or N')
	sys.exit()


#print the output in the format of alarm_clock(day,vacation):time_as_string
print("alarm_clock({},{}):{}".format(day,vacation, alarm_clock(day,vacation)))
