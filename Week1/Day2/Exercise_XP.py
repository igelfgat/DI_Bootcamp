#Exercise 1 : Favorite Numbers
"""
Instructions

Create a set called my_fav_numbers with all your favorites numbers.
Add two new numbers to the set.
Remove the last number.
Create a set called friend_fav_numbers with your friend’s favorites numbers.
Concatenate my_fav_numbers and friend_fav_numbers to a new variable called our_fav_numbers.
"""
my_fav_numbers = {1,2,7}
my_fav_numbers.add(8)
my_fav_numbers.add(9)
my_fav_numbers.remove(9)

friend_fav_numbers = {5,9,0}
our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)
print(our_fav_numbers)

#Exercise 2: Tuple
"""
Instructions
Given a tuple which value is integers, is it possible to add more integers to the tuple?
"""

# No, it is not possible. It is possible if you change tuple to the list 

#Exercise 3: List
"""
Instructions

Using this list basket = ["Banana", "Apples", "Oranges", "Blueberries"];

Remove “Banana” from the list.
Remove “Blueberries” from the list.
Add “Kiwi” to the end of the list.
Add “Apples” to the beginning of the list.
Count how many apples are in the basket.
Empty the basket.
Print(basket)
"""
basket = ["Banana", "Apples", "Oranges", "Blueberries"]
basket.remove("Banana")
basket.remove("Blueberries")
basket.append("Kiwi")
basket.insert(0, "Apples")
print(basket.count("Apples"))
basket = []
print(basket)

#Exercise 4: Floats
"""
Instructions

Recap – What is a float? What is the difference between an integer and a float?
Create a list containing the following sequence 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5 (don’t hard-code the sequence).
Can you think of another way to generate a sequence of floats?
"""

# Float is not the integer number. For example: 23.44 , 12.00001
# Integer number: 1, 444, 13133
list = [1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5]
result = [1.5]
for i in range(2,6):
    result.append(i)
    if(i + 0.5) == 5.5:
        break
    result.append(i+ 0.5)
print("result:", result)
#Exercise 5: For Loop

"""
Instructions

Use a for loop to print all numbers from 1 to 20, inclusive.
Using a for loop, that loops from 1 to 20(inclusive), print out every element which has an even index.
"""
for index, value in enumerate(range(1, 21)):
    if index % 2 == 0:
        print(value)

#Exercise 6 : While Loop
"""
Instructions

Write a while loop that will continuously ask the user for their name, unless the input is equal to your name.
"""

"""my_name = "Ilya"
user_name = ''
while user_name != my_name:
    user_name = input("Enter your name: ")
    if user_name == my_name:
        break
    else: 
        continue"""

#Exercise 7: Favorite Fruits

"""
Instructions

Ask the user to input their favorite fruit(s) (one or several fruits).
Hint : Use the built in input method. Ask the user to separate the fruit(s) with a single space, eg. "apple mango cherry".
Store the favorite fruit(s) in a list (convert the string of words into a list of words).
Now that we have a list of fruits, ask the user to input a name of any fruit.
If the user’s input is in the favorite fruits list, print “You chose one of your favorite fruits! Enjoy!”.
If the user’s input is NOT in the list, print, “You chose a new fruit. I hope you enjoy”.
"""

"""favorite_fruits = input("Enter your favorite fruit(s) using space(eg.'apple mango cherry'): ")
favorite_fruits_list = favorite_fruits.split()
print(favorite_fruits_list)
any_fruit = input("Enter any fruit: ")
if any_fruit in favorite_fruits_list:
    print("You chose one of your favorite fruits! Enjoy!")
else:
    print("You chose a new fruit. I hope you enjoy")"""


#Exercise 8: Who Ordered A Pizza ?
"""
Instructions

Write a loop that asks a user to enter a series of pizza toppings, when the user inputs ‘quit’ stop asking for toppings.
As they enter each topping, print a message saying you’ll add that topping to their pizza.
Upon exiting the loop print all the toppings on the pizza pie and what the total price is (10 + 2.5 for each topping)."""
"""pizza = []
while True:
    pizza_toping = input("Enter a series of pizza toppings, when you'll finish enter 'quit': ")
    if pizza_toping == 'quit':
        print("You ordered pizza with: ", pizza)
        print("You have to pay: ", 10 + 2.5*len(pizza))
        break
    else:
        print(f"You will add {pizza_toping} to your pizza")
        pizza.append(pizza_toping)"""

#Exercise 9: Cinemax
"""
Instructions

A movie theater charges different ticket prices depending on a person’s age.
if a person is under the age of 3, the ticket is free.
if they are between 3 and 12, the ticket is $10.
if they are over the age of 12, the ticket is $15.

Ask a family the age of each person who wants a ticket.

Store the total cost of all the family’s tickets and print it out.

A group of teenagers are coming to your movie theater and want to watch a movie that is restricted for people between the ages of 16 and 21.
Given a list of names, write a program that asks teenager for their age, if they are not permitted to watch the movie, remove them from the list.
At the end, print the final list.
"""
"""total_cost = 0
while True:
    age = input("Enter the age of each person who want a ticket(enter 'quit' when all ages are in the system): ")
    if age == "quit":
        break
    elif int(age) < 3:
        print("Free for you")
    elif 3 <= int(age) <= 12:
        print("10$")
        total_cost += 10
    elif int(age) > 12:
        print("15$")
        total_cost += 15
print("total cost: ", total_cost)"""

"""names = ["Ilya", "Artur", "Jack", "Moshe"]

for i in range(len(names)):
    age = int(input("Enter your age: "))
    name = input("Enter your name: ")
    if age < 16 or age > 21:
        names.remove(name)
        print("Your age is not allowed")
    elif name not in names:
        print("You are not in the list of names. Sorry!")
print("final list of names: ", names)"""

#Exercise 10 : Sandwich Orders

"""Instructions

Using the list below :

sandwich_orders = ["Tuna sandwich", "Pastrami sandwich", "Avocado sandwich", "Pastrami sandwich", "Egg sandwich", "Chicken sandwich", "Pastrami sandwich"]

The deli has run out of pastrami, use a while loop to remove all occurrences of “Pastrami sandwich” from sandwich_orders.
We need to prepare the orders of the clients:
Create an empty list called finished_sandwiches.
One by one, remove each sandwich from the sandwich_orders while adding them to the finished_sandwiches list.
After all the sandwiches have been made, print a message listing each sandwich that was made, such as:
I made your tuna sandwich
I made your avocado sandwich
I made your egg sandwich
I made your chicken sandwich"""

sandwich_orders = ["Tuna sandwich", "Pastrami sandwich", "Avocado sandwich", "Pastrami sandwich", "Egg sandwich", "Chicken sandwich", "Pastrami sandwich"]
finished_sandwiches = []
i = 0
while i < len(sandwich_orders):
    if sandwich_orders[i] == "Pastrami sandwich":
        sandwich_orders.remove("Pastrami sandwich")
    i += 1
print(sandwich_orders)

while sandwich_orders:
    sandwich = sandwich_orders.pop(0)
    finished_sandwiches.append(sandwich)
    print(f"I made your {sandwich}.")

    

