import sys

try:
	fhand=open('romeo.txt')
except:
	print('File cannot be opened')
	sys.exit
output_list=[]								# List to which elements added, sorted
#print('debug: ', output_list)
for line in fhand:
	words=line.rstrip().split()   			# To avoid \n and to split the line in to word list
	#print('debug: ',words)
	for word in words:
		if word in output_list: continue    # To check if word already in the list to avoid reptition
		output_list.append(word)			# If not,add the word to the list 
#print('debug: ', output_list)		
output_list.sort()
print(output_list)
