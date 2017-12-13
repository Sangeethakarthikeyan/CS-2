#fhand = open('mbox-short.txt')
fhand = open('mbox-short_modified_for_task8.4ex2.txt') # First line of the file mbox-short.txt modified
count = 0
for line in fhand:
    words = line.split()
    #print('Debug:', words)
    if len(words) == 0 : continue
    if words[0] == 'From' and len(words)>2 :   # compound logical expression with and & single if statement
        #print('Debug',words)
    	print(words[2])				   # Line to be guarded with line 9
