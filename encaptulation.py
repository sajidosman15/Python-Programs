
class Person:
    # private variable
    __name=""
    # protected variable
    _age=""

    def setName(self,name):
        self.__name=name

    def display(self):
        print(f"Name : {self.__name} Age : {self._age}")


sajid=Person()
sajid.setName("Sajid")
sajid._age=23
sajid.display()