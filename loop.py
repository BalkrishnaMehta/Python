#for i in range(10): #range(10) is 0 to 9
    #print(i)
#for j in range (5,10): #range(5,10) is 5 to 9
    #print(j)
#for k in range (0,10,2): #here 2 is stepper i.e it will step 2range(0,10,2) is 0,2,4,6,8
    #print(k)

list=[1,66,"Hello",3.42]
no=0
for l in list:
    if(l=="Hello"):
        print("Index of Hello in list is "+ str(no))
    no=no+1

dict={"Name" : "Ayush" , "roll no" : 12} 
for k,v in dict.items() :
    print(k,v)
ayush=1
while ayush!=0 :
    ayush=(int(input("enter number: ")))
    if ayush==5:
        break

