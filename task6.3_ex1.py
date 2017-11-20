word=input('Enter a word:  ')     #word as a user input
index=len(word)-1                 # index starting from the last char
while index>=0:                   # while index goes until the first character
	letter=word[index]
	print(letter)
	index=index-1
