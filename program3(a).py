def max_min(list):
    x=list[0];y=list[0]
    for j in range (len(list)): 
        if(x>list[j]):
            x=list[j]
        if(y<list[j]):
            y=list[j]
    #return x,y
    return str(x)+ " is minimum of list\n" +str(y)+ " is maximum of list"
list=[]
num=int(input("Enter number of elements in list: "))
for i in range(num):
    value=int(input("Enter value: "))
    list.append(value)
print(max_min(list))