#fhand = open('mbox-short.txt')
fhand = open('mbox-short_modified_for_task8.4ex2.txt')
count = 0
for line in fhand:
    words = line.split()
    #print('Debug:', words)
    if len(words) == 0 : continue
    if words[0] != 'From' : continue
    if len(words)<3: continue      # If this line is removed there is an error (IndexError: list index out of range)
    #print('Debug',words)
    print(words[2])				   # Line which is guarded with line 9
