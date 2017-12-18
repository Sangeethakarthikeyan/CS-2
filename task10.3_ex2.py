import sys

fname=input('Enter a file name: ')

try:
	fhandle=open(fname)
except:
	print('File cannot be opened', fname)
	sys.exit()

sample=dict()				# sample is the name of the empty dictionary
for line in fhandle:
	line=line.rstrip()		# To avoid \n at the end of each line
	words=line.split()
	if len(words)==0 :continue		# To skip empty lines (Guardian code)
	if words[0]=='From' and len(words)>6:	# To go to interested lines and guardian code for words[5]
		hour=words[5].split(':')[0]
		sample[hour]=sample.get(hour,0)+1     # add the word in dictionary if it is first occurence, else add one to value each time it occurs
#print('debug: ', sample)

sorted_list=(sorted(sample.items())) # single line code to get a sreversed orted list of (val,key) pairs 

#print('debug: ', sorted_list)


for key,val in sorted_list[:]:   	# To print all items of sorted list
	print(key,val)



