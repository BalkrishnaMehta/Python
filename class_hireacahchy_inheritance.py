''' simple class is a single derived class is of single base class
multiple more than one base class single derived class
multilevel single base has single derived and single superderived and can have more too
hirecachy single base class will have multiple derived class
hybrid can have any mixup from all of above 
Attributes of lab_assistant - designation = Lab Assistant (static), highest qualification, additional skills, year_of_joining, name_of_institute.
Attributes of office_assistant - designation Office Assistant (static), highest qualification, = year_of_joining, name_of_institute.

Attributes of peon-job_role = Office Peon (static), qualification, year_of_joining, name_of_institute.
'''
class university:
    def __init__(self,name,year_of_estd,city):
        self.name=name
        self.year_of_estd=year_of_estd
        self.city=city
class professor(university):
    designation="Professor"
    def __init__(self,highest_qualification,area_of_research,year_of_joining,year_of_experience,name_of_institute):
        super().__init__(input("Your Name: "),input("University's Year Of Establishment: "),input("University's City: "))
        self.highest_qualification=highest_qualification
        self.area_of_research=area_of_research
        self.year_of_joining=year_of_joining
        self.year_of_experience=year_of_experience
        self.name_of_institute=name_of_institute
    def display_professor(self):
        print("\n\nUniversity's Year of establishment: ", self.year_of_estd)
        print("University's city: ",self.city)
        print(self.name ,"\'s designation: ",self.designation)
        print(self.name,"\'s qualification: ", self.highest_qualification)
        print(self.name,"\'s area of research: ", self.area_of_research)
        print(self.name,"\'s year of joining: ", self.year_of_joining)
        print(self.name,"\'s year of experience: ", self.year_of_experience)
        print(self.name,"\'s Institute name: ", self.name_of_institute)
class lab_assistant(university):
    designation = "Lab_assistant"
    def __init__(self,highest_qualification,additional_skills,year_of_joining, name_of_institute):
        super().__init__(input("Your Name: "),input("University's Year Of Establishment: "),input("University's City: "))
        self.highest_qualification=highest_qualification
        self.additional_skills=additional_skills
        self.year_of_joining=year_of_joining
        self.name_of_institute=name_of_institute
    def display_lab_assistant(self):
        print("\n\nUniversity's Year of establishment: ", self.year_of_estd)
        print("University's city: ",self.city)
        print(self.name ,"\'s designation: ",self.designation)
        print(self.name,"\'s qualification: ", self.highest_qualification)
        print(self.name,"\'s addition skills: ", self.additional_skills)
        print(self.name,"\'s year of joining: ", self.year_of_joining)
        print(self.name,"\'s Institute name: ", self.name_of_institute)
class office_assistant(university):
    designation= "Office Assistant"
    def __init__(self,highest_qualification,year_of_joining,name_of_institute):
        super().__init__(input("Your Name: "),input("University's Year Of Establishment: "),input("University's City: "))
        self.highest_qualification = highest_qualification
        self.year_of_joining = year_of_joining
        self.name_of_institute = name_of_institute
    def display_office_assistant(self):
        print("\n\nUniversity's Year of establishment: ", self.year_of_estd)
        print("University's city: ",self.city)
        print(self.name ,"\'s designation: ",self.designation)
        print(self.name,"\'s qualification: ", self.highest_qualification)
        print(self.name,"\'s year of joining: ", self.year_of_joining)
        print(self.name,"\'s Institute name: ", self.name_of_institute)
class peon(university):
    designation = "Office Peon"
    def __init__(self,highest_qualification,year_of_joining,name_of_institute):
        super().__init__(input("Your Name: "),input("University's Year Of Establishment: "),input("University's City: "))
        self.highest_qualification = highest_qualification
        self.year_of_joining = year_of_joining
        self.name_of_institute = name_of_institute
    def display_peon(self):
        print("\n\nUniversity's Year of establishment: ", self.year_of_estd)
        print("University's city: ",self.city)
        print(self.name ,"\'s designation: ",self.designation)
        print(self.name,"\'s qualification: ", self.highest_qualification)
        print(self.name,"\'s year of joining: ", self.year_of_joining)
        print(self.name,"\'s Institute name: ", self.name_of_institute)
ask=input("Enter which class you want to access(professor,lab_assistant,office_assistant,peon): ")
if(ask=="professor"):
    obj=professor(input("Your Qualification: "),input("Your Area of Research: "),input("Your Year of Joining: "),input("Your Year of Experience: "),input("Your Institute Name: "))
    obj.display_professor()
elif(ask=="lab_assistant"):
    obj=lab_assistant(input("Your Qualification: "),input("Your addition skill: "),input("Your Year of Joining: "),input("Your Institute Name: "))
    obj.display_lab_assistant()
elif(ask=="office_assistant"):
    obj=office_assistant(input("Your Qualification: "),input("Your Year of Joining: "),input("Your Institute Name: "))
    obj.display_office_assistant()
elif(ask=="peon"):
    obj=peon(input("Your Qualification: "),input("Your Year of Joining: "),input("Your Institute Name: "))
    obj.display_peon()