import sys

try:
	fhand=open('mbox-short.txt')
except:
	print('File cannot be opened')
	sys.exit()
count=0
for line in fhand:
	words=line.split()
	#print('Debug: ', words)
	if len(words)==0: continue			# To avoid traceback due to blanklines
	if words[0]=='From' and len(words)>1:		# To count interested lines and guardian code for line 15						
		count=count+1
		print (words[1])
print("There are {} lines in the file with From as the first word".format(count))
