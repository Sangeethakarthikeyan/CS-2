import sys

#Function definition: cigar_party
def cigar_party(cigar,weekend):
	weekend=weekend=='Y' 	# weekend=True if input is Y/y
	if cigar>=40:				# For party success cigar>=40
		if weekend: return True		# If weekend, there is no upper limit
		elif cigar<=60:return True      # If not weekend upper limit is 60
		else: return False		# party not success if cigar>60 and if not weekend
	else: return False                      # part not success if cigar<40
	

#Get the inputs of number of cigars and if weekend or not
try:
	cigar=int(input('Enter the number of cigars: '))
except:
	print('Enter numeric data only')
	sys.exit()

weekend=input('Is it a weekend? Enter Y if yes and N if no \n').upper()
# checking if input is either Y/y or N/n
if(weekend=='Y'or weekend=='N'): print("cigar_party({},{}):{}".format(cigar,weekend,cigar_party(cigar,weekend)))  # print output
else: print('Invalid input. Enter Y or N')  # prompt to enter only Y or N if input invalid








