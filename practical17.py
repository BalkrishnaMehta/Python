# B.Tech Computer Science and Engineering(Software Engineering)
# Balkrishna Mehta
# 202103103510434
class student:
    __student_CGPA=9.2
    def display(self):
        print("The student CGPA is : ",self.__student_CGPA)
s=student()
s.display()  # Method Invocation
print("The student CGPA is: ",s.__student_CGPA)  # because of data hidind it will throw an error no attribute
