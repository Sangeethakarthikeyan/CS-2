import sys
import string

fname=input('Enter a file name: ')

try: 
    fhand = open(fname)
except:
    print('File cannot be opened', fname)
    sys.exit()

counts = dict()
for line in fhand:
    line=line.rstrip()    #To avoid \n
    line = line.translate(str.maketrans('', '', string.punctuation))  # To delete all punctuations
    line = line.lower()
    words = line.split()
    for word in words:
        letters=list(word)  # Each word is converted as a list of characters
        #print('debug: ', letters)
        for letter in letters:
            if letter.isalpha()==False: continue    # To avoid counting all numbers
            counts[letter]=counts.get(letter,0)+1   # adding each letter and its count to the dictionary
sorted_list=sorted([(count,char) for char, count in counts.items()],reverse=True)  # single line to sort based on count in decreasing order
#print('debug: ', counts)

for count,char in sorted_list[:]:       # To print char and count from the sorted list
    print(char,count)
