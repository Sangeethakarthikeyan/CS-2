print('British to American English spelling: replace ise with ize')
str = '   apologise, organise, recognise,summarise,categorise,visualise    '
print('British English:', str.strip())
print('American English:', str.strip().replace('ise','ize'))
