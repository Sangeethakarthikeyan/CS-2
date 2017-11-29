#program to find the class size of Yr1 to Yr6 for years from 2004-2017 based on the user input

print('CLASS SIZES OF YR 1 TO YR 6 FOR THE ACADEMIC YEARS FROM 2004 TO 2017')

import sys

fout=open('output_class_size.txt','w')

# open the file or print a message if the file doesnt exist
try:
	fhand=open('class_size.txt')
except:
	
	fout.write('File cannot be opened')
	sys.exit()
#Get user inputs
try:
	year=int(input('Enter any year between 1 and 6 for which class size to be found: '))
	acyear=int(input('Enter any year between 2004 and 2017: '))
except:
	fout.write('Please enter valid numeric data only')
	sys.exit()



#Give a prompt for invalid inputs
if (year not in range(1,7)) or (acyear not in range(2004,2018)):
	fout.write('Data not found. Invalid input. Please enter valid input')
	sys.exit()

# Loop for operating on each line of the file
for line in fhand:
	field=line.split()			#splitting into different fields with | as a separator
	if field[0]==str(acyear):	# For the required academic year
		fout.write("The class size of Yr {} in the year {} is {}".format(year,acyear,field[year+1]))  # field[year+1] has the data for the required year 
