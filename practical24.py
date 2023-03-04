# B.Tech Computer Science and Engineering(Software Engineering)
# Balkrishna Mehta
# 202103103510434
with open("practical24.txt","r") as f:
    var = f.read()
    words = var.split("\n")
    num = int(input("Enter number of lines you want to read from .txt file: "))
    for i in range(num):
        print(words[i])
