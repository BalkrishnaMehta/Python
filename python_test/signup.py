import re
print("                               -----------------                   ")
print("                               |    SIGNUP     |                   ")
print("                               -----------------                   ")
text_file = open("signup.txt", "w")
username = input("Enter your username of less than 10 letters must start with @: ")
a = username[0]
if  (a == '@'):
	text_file.write(username)
	text_file.write("\n")
	print("valid username")
else:
	print("not valid username")
email = input("Enter your email of the form(xyz@gmail.com): ")
if ((email[-1] == 'm') and (email[-2] == 'o') and (email[-3] == 'c') and (email[-4] == '.') and (email[-5] == 'l') and (email[-6] == 'i') and (email[-7] == 'a') and (email[-8] == 'm') and (email[-9] == 'g') and (email[-10] == '@')):
	print("valid email")
	text_file.write(email)
	text_file.write("\n")
else:
	print("invalid email")
password = input("Enter you password of more than 7 letters and must contain special character and number and atleast capital letter: ")
flag = 0
while True:  
    if (len(password)<8):
        flag = -1
        break
    elif not re.search("[a-z]", password):
        flag = -1
        break
    elif not re.search("[A-Z]", password):
        flag = -1
        break
    elif not re.search("[0-9]", password):
        flag = -1
        break
    elif not re.search("[_@$]", password):
        flag = -1
        break
    else:
        flag = 0
        print("Valid Password")
        text_file.write(password)
        break
  
if flag ==-1:
	print("Not a Valid Password")
text_file.close()


