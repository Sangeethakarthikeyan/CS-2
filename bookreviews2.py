#Import required library
import urllib.request

#Load the data from remote location (URL)
file = urllib.request.urlopen("https://gist.githubusercontent.com/twielfaert/a0972bf366d9aaf6cb1206c16bf93731/raw/dde46ad1fa41f442971726f34ad03aaac85f5414/Donna-Tartt-The-Goldfinch.csv")

f = file.read()

#Transform the bitstream into strings
text = f.decode(encoding='utf-8',errors='ignore')

lines = text.split("\n")		# list of each line in the file

reviews = dict()				# create an empty dictionary


for line in lines:				# For each line in the file
  l = line.strip().split("\t")	# split each line into 5 fields with \t as a seperator
  
  score = l[0] 					# assign first element of l as score
  id = l[1]						# assign second element of l as id
  title = l[2]					# assign third element of l as title
  review = l[3]					# assign fourth element of l as review
  reviews[id] = {"score" : score, "title" : title, "review" : review}		#assign each element of dict() as another dictionary with the key as their id

for key, val in reviews.items():
    print (reviews[key]["score"],reviews[key]["title"])						# print (access) each nested element using this statement

