#Exercise 1 : Pets
class Pets():
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'

class Bengal(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Chartreux(Cat):
    def sing(self, sounds):
        return f'{sounds}'
"""Create another cat breed named Siamese which inherits from the Cat class.
Create a list called all_cats, which holds three cat instances : one Bengal, one Chartreux and one Siamese.
Those three cats are Sara’s pets. Create a variable called sara_pets which value is an instance of the Pet class, and pass the variable all_cats to the new instance.
Take all the cats for a walk, use the walk method."""

class Siamese(Cat):
    def sing(self, sounds):
        return f'{sounds}'

def main():
    cat1 = Bengal(name="Artur", age=2)
    cat2 = Chartreux(name="Lucky", age=3)
    cat3 = Siamese(name="Sia", age=4)
    all_cats = [cat1, cat2, cat3]
    sara_pets = Pets(all_cats)
    sara_pets.walk()
if __name__ == "__main__":
    main()
#Exercise 2 : Dogs

"""Instructions

Create a class called Dog with the following attributes name, age, weight.
Implement the following methods in the Dog class:
bark: returns a string which states: “<dog_name> is barking”.
run_speed: returns the dogs running speed (weight/age*10).
fight : takes a parameter which value is another Dog instance, called other_dog. This method returns a string stating which dog won the fight. 
The winner should be the dog with the higher run_speed x weight.

Create 3 dogs and run them through your class."""

class Dog:
    def __init__(self, name, age, weight) -> None:
        self.name = name
        self.age = age
        self.weight = weight
    
    def bark(self) -> str:
        return f"{self.name} is barking"
    
    def run_speed(self) -> str:
        return int(self.weight/self.age*10)
    
    def fight(self, other_dog) -> str:
        winner = ''
        current_dog_result = self.run_speed() * self.weight
        other_dog_result = other_dog.run_speed() * other_dog.weight

        if current_dog_result > other_dog_result:
            return f"{self.name} won the fight"
        else:
            return f"{other_dog.name} won the fight"
    
def main():
    dog1 = Dog("Mike", 3, 15)
    dog2 = Dog("Rex", 2, 16)
    print(dog1.fight(dog2))
if __name__ in "__main__": 
    main()

