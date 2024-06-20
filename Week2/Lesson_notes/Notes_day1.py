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
#my_list = [2,3,1,2,"four",42,1,5,3,"imanumber"]

"""total = 0
for num in my_list:
    if isinstance(num,int):
        total += num
    else:
        continue

print(total)
print(sum(my_list))
"""
# total = 0 
# for num in my_list:
#     try:
#         total += num
#     except:
#         continue
#     else:
#         print(num) # Else will happen when the except doesn't happen
#     finally:
#         print("Happens even if there is no except")
# print(total)


# Day 4
"""



Append your first name at the end of the file
Append "SkyWalker" next to each first name "Luke"
"""
file_location = "Week2/Lesson_notes/star_wars.txt"

#Read the file line by line

contents = ""

with open(file_location) as file:
    contents = file.read()

contents_list = contents.split(
    "\n"
)  # # Read all the file and return it as a list of strings. Then split each word


print(contents_list[4])  # Read only the 5th line of the file V


with open(file_location) as file:  # Read only the 5 first characters of the file
    chars = file.read(5)
    print("First 5 chars: ", chars)


# Find out how many occurences of the names "Darth", "Luke" and "Lea" are in the file
## OPTION 1 - use dict + loop
# character_count = {"Darth": 0, "Luke": 0, "Lea": 0}

# for character in contents_list:
#     character_count[character] += 1

# print(character_count)

## OPTION 2 - Use the Counter class

from collections import Counter

character_counter = Counter(contents_list)

print(character_counter)


# Append your first name at the end of the file
with open(file_location, mode="a") as file:
    file.write("\nYossi")


# Append "SkyWalker" next to each first name "Luke"
for i, character in enumerate(contents_list):  # (0, "Darth"), (1, "Luke")
    if character == "Luke":
        contents_list[i] += " SkyWalker"


star_wars_str = "\n".join(contents_list) 

print(star_wars_str)

with open(file_location, mode="w") as file:
    file.write(star_wars_str)


# Decorator

# import os

# dir_path = os.path.dirname(os.path.realpath(__file__)) #finds the current directory path in any os
# # dir_path = 'C:\Users\julia\OneDrive\Desktop\DI-BootcampTTA17\w3\d4\the_strager.txt'


# text_name = '\\the_stranger.txt'

# with open(dir_path + text_name , mode = 'r') as file:
#     txt = file.read()

# # print(txt)

# ############################# DECORATOR: @CLASSMETHOD ####################

# class Text:
#     def __init__(self, txt_str:str)->object:
#         self.txt_str = txt_str

#     @classmethod  #classmethod
#     def from_file(cls, file_name):
#         with open(file_name, mode = 'r') as file:
#             text_file = file.read()
#             return cls(text_file)
#             # return Text(text_file) : we are returning an object of Text
        
#     def to_upper(self): #regular method justo to exemplify the difference
#         return self.txt_str.upper()

    


# text1 = Text('Hello world')
# print(text1.txt_str)
# print(text1.to_upper())

# text2 = Text.from_file('the_stranger.txt')
# print(text2.txt_str[:50])
