print('LETTER COUNT')

def count(word,letter):				#Function defintion for count: To count a given letter in a word
	count=0
	for char in word:
		if char==letter: count=count+1
	return count

#Getting user input	
word=input('Enter a word:  ')
letter=input('Enter the letter to be counted:')

print('Count:',count(word,letter))  #Function call within print function
