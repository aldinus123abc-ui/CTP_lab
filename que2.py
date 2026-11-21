numb = int(input("Enter number :"))
fact = 1
if(numb <2):
	print("Not a prime number")
else:	
	flag = 0
	for i in range(2,numb):
		flag = 0 if (numb % i == 0) else 1
	if(flag):
		print("prime")
	else:
		print("composite")
if(numb<0):
	print("Can't find factorial")
else:
	for i in range(numb):
		fact = fact * (i + 1)
	print(f"your factorial is {fact}")
	
