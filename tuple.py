x=(1,2,3,2,2) # x is tuple which can also be used without parenthesis tupple is IMMUTABLE(can't be change or append or extend)
y=(1,2,3,(4,5)) #nested tuple
z=(1,2,3,[4,5]) # list in tuple   here list can be mutaed 
a=(1) # a is int not tuple
b=(1,) # b is tuple
print(x.index(3)) #3 is element and it will print index of 3 which is 2
print(x.count(2))  # It will count how many time entered parameter is repeated
print(2 in x) # it will return true
print(2 not in x) # it will return false
b= list(x)
print(b)
