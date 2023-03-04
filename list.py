list=[1,2,3,"Hello","hi"]
print(list[-1])
print(list[-1])
print(list[1:-1])
list.append(123)
print(list)
del list[-1]
print(list)
list.extend([1,2])
print(list)
list.insert(0,99) #0 is index 99 is element
print(list)
list[0]=55 # this will overwrite
list[0:1]=[55,56]
del list #this will delete whole list
list = [1,2,3]
list.clear() #this will delete all elements
list.extend([1,22,3])
list.remove(22) #this will delete element in arguement
list.pop(0) #this will delete index in arguement
print(list)
print(list.index(3)) #print index number of element here 2
list.sort() # ascending
list.count(1) #check repetition
print(len(list))
list1=[1,2,3]
list2=list1.copy() # It will copy list
list2.reverse()   #It will reverse the list
print(list2)
list1.clear()
print(list1)

list3=[1,2,3,4,5,6,7]
print(list3[2:5])

t1 = ['a', 'b', 'c']
t2 = ['d', 'e']
t1.extend(t2)