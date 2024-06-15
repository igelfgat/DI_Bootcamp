#Exercise 1 : What Are You Learning ?

"""Instructions

Write a function called display_message() that prints one sentence telling everyone what you are learning in this course.
Call the function, and make sure the message displays correctly."""

def display_message():
    print("you are learning in this course")
display_message()

#Exercise 2: What’s Your Favorite Book ?

"""Instructions

Write a function called favorite_book() that accepts one parameter called title.
The function should print a message, such as "One of my favorite books is <title>".
For example: “One of my favorite books is Alice in Wonderland”
Call the function, make sure to include a book title as an argument when calling the function."""

def favorite_book(title):
    print(f"One of my favorite books is {title}")
favorite_book("Alice in Wonderland")


#Exercise 3 : Some Geography

"""Instructions

Write a function called describe_city() that accepts the name of a city and its country as parameters.
The function should print a simple sentence, such as "<city> is in <country>".
For example “Reykjavik is in Iceland”
Give the country parameter a default value.
Call your function."""

def describe_city(city_name, country_name = "Israel"):
    print(f"{city_name} is in {country_name}")
describe_city("Reykjavik", "Island")


#Exercise 4 : Random

"""Instructions

Create a function that accepts a number between 1 and 100 and generates another number randomly between 1 and 100. Use the random module.
Compare the two numbers, if it’s the same number, display a success message, otherwise show a fail message and display both numbers."""

import random
def generate_number(user_number):
    random_int = random.randint(1, 100)
    if random_int == int(user_number):
        print("Success")
    else:
        print("Fail")
        print("User number: ", user_number, "random number: ", random_int)

generate_number(5)

#Exercise 5 : Let’s Create Some Personalized Shirts !

"""Instructions

Write a function called make_shirt() that accepts a size and the text of a message that should be printed on the shirt.
The function should print a sentence summarizing the size of the shirt and the message printed on it, such as "The size of the shirt is <size> and the text is <text>"
Call the function make_shirt().

Modify the make_shirt() function so that shirts are large by default with a message that reads “I love Python” by default.
Call the function, in order to make a large shirt with the default message
Make medium shirt with the default message
Make a shirt of any size with a different message.

Bonus: Call the function make_shirt() using keyword arguments."""

def make_shirt(size = 'medium', msg = 'I love Python'):
    print(f"The size of the shirt is {size} and the text is '{msg}'")
make_shirt("large", "Different message")
#bonus
make_shirt(size="small", msg='I use keyword arguments')

#Exercise 6 : Magicians …

"""Instructions

Using this list of magician’s names

magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']

Create a function called show_magicians(), which prints the name of each magician in the list.
Write a function called make_great() that modifies the original list of magicians by adding the phrase "the Great" to each magician’s name.
Call the function make_great().
Call the function show_magicians() to see that the list has actually been modified."""

magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']
def show_magicians():
    magician_name_list = []
    for magician in magician_names:
        magician_name_list.append(magician.split()[0])
    print(magician_name_list)
    def make_great():
        for ind, name in enumerate(magician_name_list):
            great_name = name + " the Great"
            magician_name_list[ind] = great_name
        print(magician_name_list)
    make_great()
show_magicians()

#Exercise 7 : Temperature Advice

"""Instructions

Create a function called get_random_temp().
This function should return an integer between -10 and 40 degrees (Celsius), selected at random.
Test your function to make sure it generates expected results.

Create a function called main().
Inside this function, call get_random_temp() to get a temperature, and store its value in a variable.
Inform the user of the temperature in a friendly message, eg. “The temperature right now is 32 degrees Celsius.”

Let’s add more functionality to the main() function. Write some friendly advice relating to the temperature:
below zero (eg. “Brrr, that’s freezing! Wear some extra layers today”)
between zero and 16 (eg. “Quite chilly! Don’t forget your coat”)
between 16 and 23
between 24 and 32
between 32 and 40

Change the get_random_temp() function:
Add a parameter to the function, named ‘season’.
Inside the function, instead of simply generating a random number between -10 and 40, set lower and upper limits based on the season, eg. if season is ‘winter’, 
temperatures should only fall between -10 and 16.
Now that we’ve changed get_random_temp(), let’s change the main() function:
Before calling get_random_temp(), we will need to decide on a season, so that we can call the function correctly. 
Ask the user to type in a season - ‘summer’, ‘autumn’ (you can use ‘fall’ if you prefer), ‘winter’, or ‘spring’.
Use the season as an argument when calling get_random_temp().
"""

def get_random_temp(season):
    if season == "winter":
        temp = random.randint(-10, 16)
    elif season == "spring":
        temp = random.randint(16, 24)
    elif season == "summer":
        temp = random.randint(20, 40)
    elif season == "autumn" or season == "fall":
        temp = random.randint(16, 24)
    else:
       print("You wrote it wrong")
    return temp
def main():
    user_season = input("Choose the season: ‘summer’, ‘autumn’ (you can use ‘fall’ if you prefer), ‘winter’, or ‘spring’: ")
    temperature = get_random_temp(user_season)
    print(f"The temperature right now is {temperature} degrees Celsius.")
    if temperature < 0:
        print("Brrr, that’s freezing! Wear some extra layers today")
    elif 0 < temperature < 16:
        print("Quite chilly! Don’t forget your coat")
    elif 16 <= temperature <= 23:
        print("Nice weather, enjoy!")
    elif 24 <= temperature < 32:
        print("Warm, take your sunglasses")
    elif 32 <= temperature <= 40:
        print("It's very hot, stay home")
main()


#Bonus
"""
Bonus: Give the temperature as a floating-point number instead of an integer.
Bonus: Instead of asking for the season, ask the user for the number of the month (1 = January, 12 = December). Determine the season according to the month."""

def get_random_temp(season):
    if season == "winter":
        temp = round(random.uniform(-10, 16),2)
    elif season == "spring":
        temp = round(random.uniform(16, 24),2)
    elif season == "summer":
        temp = round(random.uniform(20, 40),2)
    elif season == "autumn":
        temp = round(random.uniform(16, 24),2)
    else:
       print("You wrote it wrong")
    return temp
def main():
    user_month = input("Enter the number of the month (1 = January, 12 = December): ")
    if user_month == "12" or user_month == "1" or user_month == "2":
        user_season = "winter"
    elif user_month == "3" or user_month == "4" or user_month == "5":
        user_season = "spring"
    elif user_month == "6" or user_month == "7" or user_month == "8":
        user_season = "summer"
    elif user_month == "9" or user_month == "10" or user_month == "11":
        user_season = "autumn"
    temperature = get_random_temp(user_season)
    print(f"The temperature right now is {temperature} degrees Celsius.")
    if temperature < 0:
        print("Brrr, that’s freezing! Wear some extra layers today")
    elif 0 < temperature < 16:
        print("Quite chilly! Don’t forget your coat")
    elif 16 <= temperature <= 23:
        print("Nice weather, enjoy!")
    elif 24 <= temperature < 32:
        print("Warm, take your sunglasses")
    elif 32 <= temperature <= 40:
        print("It's very hot, stay home")
main()

#Exercise 8 : Star Wars Quiz

"""Instructions

This project allows users to take a quiz to test their Star Wars knowledge.
The number of correct/incorrect answers are tracked and the user receives different messages depending on how well they did on the quiz.

Here is an array of dictionaries, containing those questions and answers

data = [
    {
        "question": "What is Baby Yoda's real name?",
        "answer": "Grogu"
    },
    {
        "question": "Where did Obi-Wan take Luke after his birth?",
        "answer": "Tatooine"
    },
    {
        "question": "What year did the first Star Wars movie come out?",
        "answer": "1977"
    },
    {
        "question": "Who built C-3PO?",
        "answer": "Anakin Skywalker"
    },
    {
        "question": "Anakin Skywalker grew up to be who?",
        "answer": "Darth Vader"
    },
    {
        "question": "What species is Chewbacca?",
        "answer": "Wookiee"
    }
]


Create a function that asks the questions to the user, and check his answers. Track the number of correct, incorrect answers. Create a list of wrong_answers
Create a function that informs the user of his number of correct/incorrect answers.
Bonus : display to the user the questions he answered wrong, his answer, and the correct answer.
If he had more then 3 wrong answers, ask him to play again."""

data = [
    {
        "question": "What is Baby Yoda's real name?",
        "answer": "Grogu"
    },
    {
        "question": "Where did Obi-Wan take Luke after his birth?",
        "answer": "Tatooine"
    },
    {
        "question": "What year did the first Star Wars movie come out?",
        "answer": "1977"
    },
    {
        "question": "Who built C-3PO?",
        "answer": "Anakin Skywalker"
    },
    {
        "question": "Anakin Skywalker grew up to be who?",
        "answer": "Darth Vader"
    },
    {
        "question": "What species is Chewbacca?",
        "answer": "Wookiee"
    }
]
wrong_answers = []
correct_answer = 0
incorrect_answer = 0
def quiz(): 
    global correct_answer
    global incorrect_answer
    for topic in data:
        user_answer = input(topic['question'] + ": ")
        if user_answer == topic['answer']:
            print("That's right")
            correct_answer += 1
        else:
            wrong_answers.append({
                "question": topic["question"],
                "your_answer": user_answer,
                "correct_answer": topic["answer"]
            })
            print("Not correct")
            incorrect_answer += 1
    if incorrect_answer > 3:
        new_game = input("Do you want to play again? (yes/no)")
        if new_game == "yes":
            quiz()
        else:
            print("Thanks for playing")
        
    print(wrong_answers)

quiz()