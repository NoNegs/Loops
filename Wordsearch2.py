msg = input(" Enter Your Message: ")
char = input(" What Are You Looking For?")
found=0
i=0
while i<len(msg):
	if msg[i]==char:
		found=found+1
	i=i+1
print("There is",found, char)