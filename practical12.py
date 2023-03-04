# B.Tech Computer Science and Engineering(Software Engineering)
# Balkrishna Mehta
# 202103103510434
class student:
    std_name = None
    std_age = None
    std_branch = None
    std_city = None
    def get_data(self):
        self.std_name = input("Enter Your Name: ")
        self.std_age = input("Enter Your Age: ")
        self.std_branch = input("Enter Your Branch: ")
        self.std_city = input("Enter Your City: ")
    def display(self):
        print(self.std_name)
        print(self.std_age)
        print(self.std_branch)
        print(self.std_city)
obj = student()
obj.get_data()
obj.display()
