import sys
'''
try:
    x=input("Enter no: ")
    print(x+1)
except:
    print("You haven't enter integer")
    print("The exception occured is: ", sys.exc_info())
    print("The exception occured is: ", sys.exc_info()[0])
    print("The type is: ", type(sys.exc_info()))'''

try:
    x=[0,1,2]
    print(x[3])
except:
    print("not in index")
    print("The exception occured is: ", sys.exc_info())
    print("The exception occured is: ", sys.exc_info()[0])
    print("The type is: ", type(sys.exc_info()))
finally: 
    print("This will run every time")      # Generally use for fclose
