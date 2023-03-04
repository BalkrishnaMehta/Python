class c1:
    name="Jeel"
    def display1(self):
        print("hello!👋",self.name,"from base class")
class c2(c1):
    id=123
    def display2(self):
        print("hello!👋",self.name," from derived class")
class c3(c2):
    def display3(self):
        print("hello!👋",self.name, "of ID "+ str(self.id) + " from super derived class")
b=c1()
b.display1()
d=c2()
d.display2()
s=c3()
s.display3()