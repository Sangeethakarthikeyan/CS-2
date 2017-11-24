import sys

#prompt the user for a file name
fname=input('Enter a file name: ')
# open the file and print a message if the file doesnt exist
try:
	fhand=open(fname)
except:
	print('File cannot be opened',fname)
	sys.exit()
# Read the lines of the file using for loop
for line in fhand:
	line=line.rstrip().upper()			#to strip off the whitespace in the right hand side of the string(to avoid the extra \n )
	print(line)
