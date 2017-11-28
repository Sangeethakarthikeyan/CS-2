import sys

#prompt the user for a file name
fname=input('Enter a file name: ')
# open the file or print a message if the file doesnt exist
try:
	fhand=open(fname)
except:
	print('File cannot be opened',fname)
	sys.exit()
# Loop for operating on selected lines
count=0
total=0
avg=0
for line in fhand:
	if not line.startswith('X-DSPAM-Confidence:'):
		continue						#skip the lines that do not startwith the phrase
	#code to operate on selected lines 								
	count=count+1						# to count the selected lines 
	colonpos=line.find(':')				# to find the position of :
	newlinepos=line.find('\n',colonpos)	# to find the position of \n
	number=line[colonpos+1:newlinepos]	# to extract the string that we are interested in
	fnumber=float(number)				# to convert the string to float inorder to operate on it
	total=total+fnumber					# finding the sum
if count!=0: avg=total/count			# to avoid division by zero exception # to compute average
					
print('Average SPAM Confidence: ', round(avg,12))	# to print the average
