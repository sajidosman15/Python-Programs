class Person:
    name=""
    age=""

    def __init__(self,name,age):
        self.name=name
        self.age=age

    def display(self):
        print(f"Name : {self.name}")
        print(f"Age : {self.age}")

class Student(Person):
    gpa=""

    def __init__(self,name,age,gpa):
        super().__init__(name,age)
        self.gpa=gpa

    def display(self):
        super().display()
        print(f"GPA : {self.gpa}")

sajid=Student("Sajid",23,3.9)
sajid.display()