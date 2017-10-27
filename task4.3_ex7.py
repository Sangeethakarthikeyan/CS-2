import sys

# function definition to compute grade
def computegrade(s):
	if s>=0.0 and s<=1.0:
		if s>=0.9: g='A'
		elif s>=0.8: g='B'
		elif s>=0.7: g='C'
		elif s>=0.6: g='D'
		else: g='F'
	else: g='Bad score'
	return g

# actual program
#Get input as score
try: score=float(input('Enter score:'))
except:
	print('Bad score')
	sys.exit()
# Function call for computegrade
grade=computegrade(score)
print(grade) 
