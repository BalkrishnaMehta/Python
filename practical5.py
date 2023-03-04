# B.Tech Computer Science and Engineering(Software Engineering)
# Balkrishna Mehta
# 202103103510434
txt = "Hello, welcome to my world."
print("txt after using .upper: ")
print(txt.upper())
print("txt after using .lower: ")
print(txt.lower())
str1 = txt.split(" ")
print("string after splitting txt: ")
print(str1)
jointer = ' '
str2 = jointer.join(str1)
print("Joining string from list = str2: ")
print(str2)
print("comparing words in string and return number of letters in word: ")
print(txt.find("welcome"))
print("string after replacing world by home: ")
print(txt.replace("world", "home"))
