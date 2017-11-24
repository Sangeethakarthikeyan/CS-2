import sys

#prompt the user for a file name
fname=input('Enter a file name: ').lower()
if fname=='na na boo boo':
		print("NA NA BOO BOO TO YOU - You have been punk'd")
		sys.exit()
# open the file and print a message if the file doesnt exist
try:
	fhand=open(fname)
except:
	print('File cannot be opened',fname)
	sys.exit()
# Read the lines of the file using for loop
for line in fhand:
	line=line.rstrip().upper()
	print(line)
