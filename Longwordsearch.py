msg = input(" Enter Your Message: ")
what = input(" What Are You Looking For?")
found=0
i=0
while i<len(msg):
	if what in msg:
		found=found+1
	i=i+1
print(found)