def censor(txt,censor_wd):
	words=txt.split()
	#print(type(words)) # here type is list. It becomes a string after applying join method later
	for i, wd in enumerate(words):
		if wd==censor_wd:
			words[i]= '*' * len(censor_wd) #making the change in the list itslef (my mistake is changing the iteration variable only)
			
	words=' '.join(words)  #joined_list=separator.join(list)

	print(words) # It becomes a string after applying join method later
	#print(type(words))

censor("this hack is wack hack", "hack")
