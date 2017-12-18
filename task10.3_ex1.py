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
	if words[0]=='From' and len(words)>2:			# To go to interested lines and guardian code for words[1]
		sample[words[1]]=sample.get(words[1],0)+1     # add the word in dictionary if it is first occurence, else add one to value each time it occurs

sorted_list=(sorted([(val,key) for key, val in sample.items()],reverse=True)) # single line code to get a sreversed orted list of (val,key) pairs 

for val,key in sorted_list[:1]:    # To print the first occuring element as key,value pair
	print(key,val)

