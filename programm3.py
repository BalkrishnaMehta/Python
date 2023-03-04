import os
def fun(file):
    file.close()
    lst=[]
    fle = open('min_max.txt', 'r')
    lst=(fle.readlines())
    x=int(lst[0])
    y=int(lst[0])
    for j in range (len(lst)): 
        if(x>int(lst[j])):
            x=lst[j]
        if(y<int(lst[j])):
            y=int(lst[j])
    os.remove("min_max.txt")
    return str(x)+ " is minimum of list\n" +str(y)+ " is maximum of list"


file = open('min_max.txt', 'w')
num=int(input("Enter number of elements in list: "))
for i in range(num):
    value=input("Enter Value: ")
    file.write(value+"\n")
print(fun(file))
