# B.Tech Computer Science and Engineering(Software Engineering)
# Balkrishna Mehta
# 202103103510434
print("Creation of List: ")
list1=[1,5,4,2,3]
list1.append(6)
print("List1 after appending 6: ") # This will add one element to list
print(list1)
list1.extend([6,8])     # This will add more than one element to list
print("extending List1 with 6,7: ")
print(list1)
list1.insert(4,0) #4 is index 0 will be element of list
print("List1 after inserting 0 at index 4: ")
print(list1)
list1.remove(0) #This will delete element in arguement from list
print("List1 after removing 0: ")
print(list1)
print("Index of 3 in list1: ")
print(list1.index(3)) # Index of Element in arguement
print("repetition of 6 in list1: ")
print(list1.count(6)) #check repetition of Element in arguement
list1.sort() # ascending
print("List1 after sorting elements in ascending order: ")
print(list1)
list1.reverse()   #It will reverse the list
print("List1 after reversing list1: ")
print(list1)
list2=list1.copy()
print("Copied List2 from List1")
print(list2)
list2.clear() # This will delete all elements from list
print("List2 after using list2.clear")
print(list2)
print("Element at Index 1 in list1")
print(list1[1])
print("Element at Index 1 in list1")
print(list1[-1])
print("Element between index 1 and 4 excluding 4:")
print(list1[1:4])
print("List1: ")
print(list1)
list1[1] = 33
print("Updation of list1 at index1: ")
print(list1)
del list1[1]
print("Deleting element from index 1 from list1")
print(list1)
del list1[1:4]
print("Deleting element from index 1 to 4 excluding 4 from list1")
print(list1)
