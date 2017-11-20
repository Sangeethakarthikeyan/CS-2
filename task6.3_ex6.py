print('British to American English spelling: replace ise with ize')

str = '   apologise, organise, recognise,summarise,categorise,visualise    '

print('British English:', str.strip()) # print without white spaces 

print('American English:', str.strip().replace('ise','ize'))   # print without white spaces and replace 'ise' with 'ize'
