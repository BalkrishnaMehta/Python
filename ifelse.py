pas=input("enter password: ")
if pas=="cgpit@123":
	print(str(pas)+" is correct")
	
num=(int(input("Enter Number:")))
if num<5:
	print(str(num)+" is less than 5")
elif num==5:
	print(str(num)+" is equal to 5")
else :
	print(str(num)+" is greater than 5")

enroll=(int(input("Enter last three enrollment no enter 300 or 301: ")))
password=(input("Enter Password: "))
if enroll==300 :
	if password=="cgpit@123":
		print(str(enroll) + password + "Verified")
	elif password=="CGPIT@123":
		print("Your capslock is on renter password")
		password=(input("Enter Password: "))
	else:
		print("wrong password")
		password=(input("Enter Password: "))
if enroll==301 :
	if password=="stud@123":
		print(str(enroll) + password + "Verified")
	elif password=="STUD@123":
		print("Your capslock is on renter password")
		password=(input("Enter Password: "))
	else:
		print("wrong password")
		password=(input("Enter Password: "))