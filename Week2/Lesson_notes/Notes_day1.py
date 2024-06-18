#Exercise

"""Analyse the code below. What will be the output ?

Explain the goal of the methods

Create a method that modifies the name of the person"""

"""
NAME = str
"""

"""class Person():
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
print(first_person.name)"""



# Day2
"""Try to recreate the class explained below:

We have a class called Door that has an attribute of is_opened declared when an instance is initiated.

We can create a class called BlockedDoor that inherits from the base class Door.

We just override the parent class's functions of open_door() and close_door() with our own BlockedDoor version of those functions,
which simply raises an Error that a blocked door cannot be opened or closed."""

"""class Door:
    def __init__(self, is_opened = True) -> None:
        self.is_opened = is_opened

    def open_door(self):
        self.is_opened = True
        return self.is_opened
        #print("the door is now open")
    
    def close_door(self):
        self.is_opened = False
        print("the door is now closed")


class BlockedDoor(Door):
    def open_door(self):
        raise Exception("a blocked door can't be open")
        

    def close_door(self):
        raise Exception("a blocked door can't be closed")

door1 = Door()
door1.close_door()
print(door1.is_opened)

door2 = BlockedDoor()
door2.close_door()
"""

#without try except
my_list = [2,3,1,2,"four",42,1,5,3,"imanumber"]

"""total = 0
for num in my_list:
    if isinstance(num,int):
        total += num
    else:
        continue

print(total)
print(sum(my_list))
"""
total = 0 
for num in my_list:
    try:
        total += num
    except:
        continue
    else:
        print(num) # When except did work
    finally:
        print("Happens even if there is no except")
print(total)
