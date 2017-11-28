import sys

#prompt the user for a file name
fname=input('Enter a file name: ')
# open the file or print a message if the file doesnt exist
try:
	fhand=open(fname)
except:
	print('File cannot be opened',fname)
	sys.exit()

# Loop for operating on each line of the file
total=0
for line in fhand:
	field=line.split('|')			#splitting into different fields with | as a separator
		if field[1]=='Central':		# If second field is central
			number=int(field[2])	# assign the third field to number 
			total=total+number		# To find the total
print('Total approvals in Central district of the year 2016: ', total)	
