class staff:
    def __init__(self,name,age):
        self.name=name
        self.age=age
class teacher(staff):
    def __init__(self,salary,department):
        self.salary=salary
        self.dep=department
        super().__init__(input("Enter Name: "),int(input("Enter Age: ")))
    def display(self):
        print("\n\n")
        print("Teacher's Name: ",self.name)
        print("Teacher's age: ",self.age)
        print("Teacher's salary: ",self.salary)
        print("Teacher's Department: ",self.dep)

obj=teacher(int(input("Enter Salary: ")),input("Enter Department: "))
obj.display()

