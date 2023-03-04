# B.Tech Computer Science and Engineering(Software Engineering)
# Balkrishna Mehta
# 202103103510434
def add(*list):
    j=0
    for i in range (len(list)):
        j=j+ list[i]
    return j

def sub(a,b):
    return a-b

def mul(*list):
    j=1
    for i in range (len(list)):
        j=j* list[i]
    return j

def div(a,b):
    return a/b

def even_or_odd(a):
        if (a%2==0):
            return " is even."
        else :
            return " is odd."
def main():
    ask1=input("add or sub or mul or div or exit: ")
    if (ask1=="add"):
        size=int(input("Enter Number of Input: "))
        list1=[]
        for j in range (size):
            value=int(input("Enter value: "))
            list1.append(value)
        print(add(*list1))
        main()
    if (ask1=="sub"):
        var1=int(input("Enter number: "))
        var2=int(input("Enter number: "))
        print(sub(var1,var2))
        main()
    if (ask1=="mul"):
        size1=int(input("Enter Number of Input: "))
        list1=[]
        for j in range (size1):
            value1=int(input("Enter value: "))
            list1.append(value1)
        print(mul(*list1))
        main()
    if (ask1=="div"):
        var3=int(input("Enter number: "))
        var4=int(input("Enter number: "))
        print(div(var3,var4))
        main()
    if (ask1 == "exit"):
        pass
main()
