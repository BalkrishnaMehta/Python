import os
file = open('min_max.txt', 'w')
while True:
    try: 
        x=input("Enter Value(Alphabet will break loop): ")
        int(x)
        file.write(x+"\n")
    except:
        break

def min_max(file):
    file.close()
    lst=[]
    fle = open('min_max.txt', 'r')
    for x in fle:
        lst.append(int(x))
    x=int(lst[0])
    y=int(lst[0])
    for j in range (len(lst)): 
        if(x>int(lst[j])):
            x=lst[j]
        if(y<int(lst[j])):
            y=int(lst[j])
    os.remove("min_max.txt")
    return str(x)+ " is minimum of list\n" +str(y)+ " is maximum of list"

print(min_max(file))
