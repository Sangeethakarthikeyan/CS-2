import sys

#Get the inputs of number of cigars and if weekend or not
try:
	cigar=int(input('Enter the number of cigars: '))
except:
	print('Enter numeric data only')
	sys.exit()

weekend=input('Is it a weekend? Enter Y if yes and N if no \n')

# checking if input is either Y/y or N/n
if(weekend=='Y' or weekend=='y' or weekend=='N' or weekend=='n'):
	weekend=(weekend=='Y' or weekend=='y') 	# weekend=True if input is Y/y
	
	if cigar>=40:							# For party success cigar>=40
		if weekend:party_success=True		# If weekend, there is no upper limit
		elif cigar<=60:party_success=True   # If not weekend upper limit is 60
		else: party_success=False			# party not success if cigar>60 and if not weekend
	else: party_success=False               # part not success if cigar<40

	print("cigar_party({},{}):{}".format(cigar,weekend,party_success))  # print output

else: print('Invalid input. Enter Y or N')  # prompt to enter only Y or N if input invalid

