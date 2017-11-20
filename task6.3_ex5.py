str = 'X-DSPAM-Confidence:0.8475'   #Given string
colon_pos=str.find(':')             #To find the index of colon
float_value=float(str[colon_pos+1:len(str)])    # To convert to float the substring starts from next character of : to the end
print(float_value)
