import sys

try:
	fhandle=open('romeo.txt')
except:
	print('File cannot be opened')
	sys.exit()

sample=dict()				# sample is the name of the empty dictionary
for line in fhandle:
	line=line.rstrip()		# To avoid \n at the end of each line
	words=line.split()
	for word in words:
		sample[word]=sample.get(word,0)+1		# add the word in dictionary if it is first occurence, else add one to value each time it occurs
print(sample)

check=input('\n \n Enter a word to be checked if in dictionary or not: ')  
print(check in sample)    # True if word exists and False if not





