class area:
    def display(self,a=None,b=None):
        if(a!=None and b==None):
            print("Square Area is: ",a*a)
        if(b!=None):
            print("Rectangle Area is: ",a*b)
obj=area()
obj.display(10)
obj.display(10,20)