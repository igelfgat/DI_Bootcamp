#Exercise 3 : Dogs Domesticated

"""Instructions

Create a new python file and import your Dog class from the previous exercise.
In the new python file, create a class named PetDog that inherits from Dog.
Add an attribute called trained to the __init__ method, this attribute is a boolean and the value should be False by default.
Add the following methods:
    train: prints the output of bark and switches the trained boolean to True
    
    play: takes a parameter which value is a few names of other Dog instances (use *args). 
    The method should print the following string: “dog_names all play together”.

do_a_trick: If the dog is trained the method should print one of the following sentences at random:
“dog_name does a barrel roll”.
“dog_name stands on his back legs”.
“dog_name shakes your hand”.
“dog_name plays dead”."""
import random
from Exercies_XP import Dog
class PetDog(Dog):
    def __init__(self, name, age, weight) -> None:
        super().__init__(name, age, weight)
        self.trained = False

    def train(self):
        print(self.bark())
        self.trained = True
        command_list = [f"{self.name} does a barrel roll", f"{self.name} stands on his back legs", f"{self.name} shakes your hand", f"{self.name} plays dead"]
        print(random.choice(command_list))

    
    def play(self, *few_dog_names):
        dog_names = ''
        for i, dog_name in enumerate(few_dog_names):
            if i > 0:
                if i == len(few_dog_names) - 1:
                    dog_names += ' and '
                else:
                    dog_names += " , "
            dog_names += dog_name
        print(f"{self.name},{dog_names} all play together")
    


def main():
    dog1 = PetDog("Rokki", 5, 20)
    dog2 = PetDog("Molly", 6, 21)
    dog1.train()
    dog2.play("Luffy", "Mikky")
if __name__ in "__main__":
    main()

#Exercise 4 : Family

"""Instructions

Create a class called Family and implement the following attributes:

members: list of dictionaries
last_name : (string)

Implement the following methods:

born: adds a child to the members list (use **kwargs), don’t forget to print a message congratulating the family.
is_18: takes the name of a family member as a parameter and returns True if they are over 18 and False if not.
family_presentation: a method that prints the family’s last name and all the members’ details.

Create an instance of the Family class, with the last name of your choice, and the below members. Then call all the methods you created in Point 2.

    [
        {'name':'Michael','age':35,'gender':'Male','is_child':False},
        {'name':'Sarah','age':32,'gender':'Female','is_child':False}
    ]"""

class Family:
    def __init__(self, members: list, last_name: str) -> None:
        self.members = members
        self.last_name = last_name

    def born(self, **kwargs):
        self.members.append(kwargs)
        print(f"Congratulations to the {self.last_name} family on the birth of {kwargs['name']}!")
        
    def is_18(self, name: str):
        for member in self.members:
            if member['name'] == name:
                return member['age'] > 18
        return False


    def family_presentation(self):
        print(f"The {self.last_name} family members:")
        for member in self.members:
            print(member)

    
def main():   
    my_family = Family( [
            {'name':'Michael','age':35,'gender':'Male','is_child':False},
            {'name':'Sarah','age':32,'gender':'Female','is_child':False}
        ],
        "Smith")

    my_family.born(name='Ilya', age=0, gender='Male', is_child=True)
    print(my_family.is_18('Michael'))
    my_family.family_presentation()
if __name__ in "__main__":
    main()


#Exercise 5 : TheIncredibles Family
    
#Create a class called TheIncredibles. This class should inherit from the Family class:
#This is no random family they are an incredible family, therefore the members attributes, will be a list of dictionaries containing the additional keys : power and incredible_name. (See Point 4)
class TheIncredibles(Family):
    def __init__(self, members: list, last_name: str) -> None:
        super().__init__(members, last_name)
   # Add a method called use_power, this method should print the power of a member only if they are over 18 years old. If not raise an exception (look up exceptions) which stated they are not over 18 years old. 
    def use_power(self, name):
        for member in self.members:
            if member['name'] == name:
                if member['age'] > 18:
                    print(f"{member['name']} has {member['power']} power")
                else:
                    raise Exception(f"{name} is not over 18 years old.")
    # Add a method called incredible_presentation which :
        # Print a sentence like “*Here is our powerful family **”
        # Prints the family’s last name and all the members’ details (ie. use the super() function, to call the family_presentation method)
    def incredible_presentation(self):
        print("Here is our powerful family")
        print(super().family_presentation())

def main():
#Create an instance of the Incredibles class, with the “Incredibles” last name, and the below members.
# [
#     {'name':'Michael','age':35,'gender':'Male','is_child':False,'power': 'fly','incredible_name':'MikeFly'},
#     {'name':'Sarah','age':32,'gender':'Female','is_child':False,'power': 'read minds','incredible_name':'SuperWoman'}
# ]

    incredible_family = TheIncredibles(  [
        {'name':'Michael','age':35,'gender':'Male','is_child':False,'power': 'fly','incredible_name':'MikeFly'},
        {'name':'Sarah','age':32,'gender':'Female','is_child':False,'power': 'read minds','incredible_name':'SuperWoman'}
    ], "Incredibles")
    
    # Call the incredible_presentation method.

    incredible_family.incredible_presentation()
    # Use the born method inherited from the Family class to add Baby Jack with the following power: “Unknown Power”.

    incredible_family.born(name='Jack', age=0, gender='Male', is_child=True, power="Unknown Power", incredible_name="BabyJack")
    # Call the incredible_presentation method again
    incredible_family.incredible_presentation()

if __name__ in "__main__":
    main()

