# B.Tech Computer Science and Engineering(Software Engineering)
# Balkrishna Mehta
# 202103103510434
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
value=input("Enter Elements in List and Enter exit to end loop\n: ")
while(True):
    list.append(int(value))
    value=input(": ")
    if (value == "exit"):
        break
print(max_min(list))
