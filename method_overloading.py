class greet:
    def display(self,name=None):
        if(name==None):
            print("Welcome")
        else:
            print("Welcome ",name)
obj=greet()
obj.display()
#obj.display("Dhruv")
