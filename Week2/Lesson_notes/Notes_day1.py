#Exercise

"""Analyse the code below. What will be the output ?

Explain the goal of the methods

Create a method that modifies the name of the person"""

"""
NAME = str
"""

class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_details(self):
        print("Hello my name is " + self.name)


    def modifies_name(self, new_name: str) -> None:
        self.name = new_name
        


first_person = Person("John", 36)
first_person.show_details()
first_person.modifies_name("Ben")
print(first_person.name)