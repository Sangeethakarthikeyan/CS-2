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
	linepos1=line.find('|')				# to find the position of first |
	cutline=line[linepos1+1:]			# to extract the part of the line which starts with the district name 
	
	if not cutline.startswith('Central'):	# to check if the district name is central (if the extracted line startswith central)
		continue						#skip the lines that do not startwith central
	
	#code to operate on selected lines which startswith central								
	
	linepos2=line.find('|', linepos1+1)	# Find the position of second | in the whole line	
	linepos3=line.find('|', linepos2+1)	# Find the position of third | in the whole line
	number=int(line[linepos2+1:linepos3])	# Extract the number between second | and third |
	total=total+inumber					# To find the total

						
print('Total approvals in Central district of the year 2016: ', total)	# to print the total
