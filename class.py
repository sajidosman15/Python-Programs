class Student:
    roll=""
    gpa=""

    # def setvalue(self,gpa,roll):
    #     self.gpa=gpa
    #     self.roll=roll

    # constructor
    def __init__(self,gpa,roll):
        self.gpa=gpa
        self.roll=roll

    def display(self):
        print(f"{self.gpa} {self.roll}")

sajid=Student(3.9,1)
# sajid.setvalue(3.4,3)
sajid.display()

