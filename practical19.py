# B.Tech Computer Science and Engineering(Software Engineering)
# Balkrishna Mehta
# 202103103510434
class base:
    def display(self):
        print("I am  a base class.")
class derived(base):
    def display(self):
        print("I am a derived class.")
        #super().display() #this is used to invokes overided method
obj=derived()
obj.display()
