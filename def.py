'''def Ayush():
    print("hello world")
    return
Ayush()

def sum(a,b):
    i=a+b
    return i

y=int(input("Enter num1: "))
z=int(input("Enter num2: "))

u=sum(y,z)
print("sum i = "+ str(u))'''

def fun(*g): #g will be class tupple
    print(g)
    return 0
a=1;b=3;c=4  
fun(a,b,c)      #here list,tupples or arbitrary or multiple numbers of variable can be passed