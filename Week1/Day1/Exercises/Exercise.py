
#Exercise 1 : Hello World
"""
Instructions
Print the following output in one line of code:
Hello world
Hello world
Hello world
Hello world"""
print("Hello world \n Hello world \n Hello world \n Hello world")

# Exercise 2 : Some Math
"""
Instructions
Write code that calculates the result of: (99^3)*8 (meaning 99 to the power of 3, times 8).
"""
print((99**3)*8)

# Exercise 3 : What Is The Output ?
"""
Instructions
Predict the output of the following code snippets:
>>> 5 < 3
>>> 3 == 3
>>> 3 == "3"
>>> "3" > 3
>>> "Hello" == "hello"
"""
print("False", "True", "False","False or Error", "False")

#Exercise 4 : Your Computer Brand
"""
Instructions
Create a variable called computer_brand which value is the brand name of your computer.
Using the computer_brand variable print a sentence that states the following: "I have a <computer_brand> computer".
"""
computer_brand = "Mac"
print(f"I have a {computer_brand} computer")

# Exercise 5 : Your Information
"""
Instructions
Create a variable called name, and set it’s value to your name.
Create a variable called age, and set it’s value to your age.
Create a variable called shoe_size, and set it’s value to your shoe size.
Create a variable called info and set it’s value to an interesting sentence about yourself. The sentence must contain all the variables created in parts 1, 2 and 3.
Have your code print the info message.
Run your code
"""
my_name = "Ilya"
age = 25
shoe_size = 45
info = f"Hi, My name {my_name}, I am {age} years old. When I served in the army I had a shoes with {shoe_size} size"
print(info)

# Exercise 6 : A & B
"""
Instructions
Create two variables, a and b.
Each variable value should be a number.
If a is bigger then b, have your code print Hello World.
"""
a = 10
b = 6
if a > b:
    print("Hello world")
else:
    print("No, now i don't reture Hello")


#Exercise 7 : Odd Or Even
"""
Instructions
Write code that asks the user for a number and determines whether this number is odd or even.
"""
number = input("Enter your number: ")
if int(number) % 2 == 0:
    print("Even number")
else:
    print("Odd number")

#Exercise 8 : What’s Your Name ?
"""
Instructions
Write code that asks the user for their name and determines whether or not you have the same name, print out a funny message based on the outcome.
"""
user_name = input("Enter your name, my friend: ")
if my_name == user_name:
    print("Hi my friend Ilya")
else:
    print(f"Hey {user_name}")

#Exercise 9 : Tall Enough To Ride A Roller Coaster
"""
Instructions
Write code that will ask the user for their height in centimeters.
If they are over 145cm print a message that states they are tall enough to ride.
If they are not tall enough print a message that says they need to grow some more to ride.
"""

height_in_centimeters = input(" Enter your height in centimeters: ")
if int(height_in_centimeters) > 145:
    print("You are tall enough to ride")
elif int(height_in_centimeters) < 145:
    print("You need to grow some more to ride")

