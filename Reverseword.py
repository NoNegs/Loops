word=" "
msg = input(" Enter Your Message: ")
i=0
while i<len(msg):
	if msg[i]==" ":
		print(word)
		word= " "
	else:
		word=word + msg[i]
	i=i+1
print(word)
	
	