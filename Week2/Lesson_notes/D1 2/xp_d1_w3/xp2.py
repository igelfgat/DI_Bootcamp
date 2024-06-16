# Create a class called Dog.
class Dog:

    # In this class, create an __init__ method that takes two parameters : name and height. This function instantiates two attributes, which values are the parameters.
    def __init__(self, name: str, height: float) -> None:
        self.name = name
        self.height = height

    # Create a method called bark that prints the following string “<dog_name> goes woof!”.
    def bark(self) -> None:
        print(f"{self.name} goes woof!")

    # Create a method called jump that prints the following string “<dog_name> jumps <x> cm high!”. x is the height*2.
    def jump(self) -> None:
        jump_height = self.height * 2
        print(f"{self.name} jumps {jump_height} cm high!")

    def present(self):
        print(f"Dog name: {self.name}. Height: {self.height}")


# def present_dog(dog: Dog) -> None:
#     print(f"Dog name: {dog.name}. Height: {dog.height}")


def get_biggest_dog(dogs: list[Dog]) -> Dog:
    biggest_dog = max(dogs, key=lambda dog: dog.height)
    return biggest_dog


# Outside of the class, create an object called davids_dog. His dog’s name is “Rex” and his height is 50cm.
def main():

    david_dog = Dog(name="Rex", height=50)
    # Print the details of his dog (ie. name and height) and call the methods bark and jump.
    david_dog.present()

    sarahs_dog = Dog("Teacup", 20)
    sarahs_dog.present()

    # Create an if statement outside of the class to check which dog is bigger. Print the name of the bigger dog.
    biggest_dog = get_biggest_dog([david_dog, sarahs_dog])
    print(f"{biggest_dog.name} is the biggest dog in town!")


if __name__ == "__main__":
    main()
