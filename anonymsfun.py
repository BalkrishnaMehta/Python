# Anonyms function or lambda function
'''b=lambda j : j+1
print(b(9))

c=lambda k,l,m : k*l*m
print(c(2,3,4))'''

d=lambda p : print(p+1)
d(4)

list1=[1,2,3,4,5,9,8,7,6]
list2=tuple(filter(lambda n : (n%2==0), list1))
list4=list(filter(lambda n : (n%2==0), list1))
print(list2)
print(type(list2))
print(list4)
print(type(list4))

list3=list(map((lambda u : (u*2)), list1))
print(list3)
