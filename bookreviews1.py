#Import required library
import urllib.request    # extensible library for opening URLs

#Load the data from remote location (URL)
file = urllib.request.urlopen("https://gist.githubusercontent.com/twielfaert/a0972bf366d9aaf6cb1206c16bf93731/raw/dde46ad1fa41f442971726f34ad03aaac85f5414/Donna-Tartt-The-Goldfinch.csv")

f = file.read()  # file.read(n) reads n number of characters in the file. If n is blank it reads the entire file
                 #print('debug: ', type(f)) note that type(f) is bytes

#Transform the bitstream into strings
text = f.decode(encoding='utf-8',errors='ignore')   # decode method returns a decoded string stored in the name text. errors='strict' is the default and it means raise the Unicode error incase of encoding errors

                                                    #print('debug: ', type(text))  # <class 'str'>

lines = text.split("\n")  							#It returns a list. Each entry in the list is the string (each line in the file as \n is the seperator. whitespace is the default seperator
													#print('debug: ', type(lines))	<class 'list'>
counts = dict()	#create a new dictionary named counts
counter = 0

for line in lines:									# For each line in the file (each element in lines list)
  l = line.strip().split("\t")						# strip() removes all whitespace at the start and end, including spaces, tabs, newlines and carriage returns. split('\t') creates a list of strings in each line (separator being \t)
  													#print('debug: ', l) # ['5.0', '', '','']
  
  score = l[0] 										#assign the first element of the the list as score
  id = l[1]											#assign the second element of the the list as id
  title = l[2]										#assign the third element of the the list as title
  review = l[3]										#assign the fourth element of the the list as review
  
  counts[score] = counts.get(score, 0) + 1			# add the score to the list for its first ocuurence with value 1 and for the next occurences increment the value by 1
  counter = counter + 1 							# counter counts the number of elements in the lines list 

print(str(counter))									# prints the final value of counter (after converting the int to str)
print(str(len(lines)))								# prints the value of len(lines) -(after converting it into string) !!! Both counter and len(lines) are same- it means the loop executed for all entries of the list
	


for key, val in counts.items():						# prints the (key,value) of counts dictionary. That is (score,no of occurences of the score in the file) 
    print (key, val)
