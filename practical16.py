# B.Tech Computer Science and Engineering(Software Engineering)
# Balkrishna Mehta
# 202103103510434
class C:
    def __init__(self,c_learning,c_name_professor):
        self.c_learning = c_learning
        self.c_name_professor = c_name_professor
class Python:
    def __init__(self,py_learning,py_name_professor):
        self.py_learning = py_learning
        self.py_name_professor = py_name_professor
class Web_Designing:
    def __init__(self,wd_learning,wd_name_professor):
        self.wd_learning = wd_learning
        self.wd_name_professor = wd_name_professor
class student(C,Python,Web_Designing):
    std_college = "Asha M.Tarsadia Institute Of Computer Science"
    def __init__(self,std_name,std_enroll_no,std_course, c_learning, c_name_professor,py_learning,py_name_professor,wd_learning,wd_name_professor):
        self.std_name = std_name
        self.std_enroll_no = std_enroll_no
        self.std_course = std_course
        C.__init__(self,c_learning,c_name_professor)
        Python.__init__(self,py_learning,py_name_professor)
        Web_Designing.__init__(self,wd_learning,wd_name_professor)

    def display(self):
        print("-----------------------------------------------------------------")
        print("|   Welcome to ",self.std_college,"  |")
        print("-----------------------------------------------------------------")
        print("Name: ",self.std_name)
        print("Enrollment No: ",self.std_enroll_no)
        print("Course: ",self.std_course)
        print("-----------------------------------------------------------------\n")
        print(self.std_name,"\'s Learning in C: ")
        for i in range (len(self.c_learning)) :
            print("-",self.c_learning[i])
        print("Professor's Name: ",self.c_name_professor)
        print("-----------------------------------------------------------------\n")
        print(self.std_name,"\'s Learning in Python: ")
        for j in range (len(self.py_learning)) :
            print("-",self.py_learning[j])
        print("Professor's Name: ",self.py_name_professor)
        print("-----------------------------------------------------------------\n")
        print(self.std_name,"\'s Learning in Web Designing: ")
        for k in range (len(self.wd_learning)) :
            print("-",self.wd_learning[k])
        print("Professor's Name: ",self.wd_name_professor)
        print("-----------------------------------------------------------------\n")

        

list_c=[]
list_py=[]
list_wd=[]
name = input("Enter your name: ")
enroll = input("Your Enrollment No: ")
course = input("Your Course Name: ")
print("Your learning in c: ",end="")
while(1):
    tmp1=input("-")
    if(tmp1=="exit"):
        break
    list_c.append(tmp1)
professor_of_c = input("Professor of C name: ")
print("Your learning in Python: ",end="")
while(1):
    tmp2=input("-")
    if(tmp2=="exit"):
        break
    list_py.append(tmp2)
professor_of_py = input("Professor of Python name: ")
print("Your learning in Web Desgning: ",end="")
while(1):
    tmp3=input("-")
    if(tmp3=="exit"):
        break
    list_wd.append(tmp3)
professor_of_wd = input("Professor of Web designing name: ")
obj=student(name,enroll,course,list_c,professor_of_c,list_py,professor_of_py,list_wd,professor_of_wd)
obj.display()
