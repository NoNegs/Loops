msg = input(" Enter Your Message: ")
find = input(" What Are You Looking For?")
found=0
i=0
while i<len(msg):
	if msg[i]==find[0]:
		if msg[i:i+len(find)]==find:
			found=found+1
			i=i+len(find)-1
	i=i+1
print(found)