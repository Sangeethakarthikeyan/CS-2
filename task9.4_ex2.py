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
	if words[0]=='From' and len(words)>3:				# To go to interested lines and guardian code for words[2]
		sample[words[2]]=sample.get(words[2],0)+1     # add the word in dictionary if it is first occurence, else add one to value each time it occurs
print(sample)
