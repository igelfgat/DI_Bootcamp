#Exercise 1: Currencies
class Currency:
    def __init__(self, currency, amount):
        self.currency = currency
        self.amount = amount
    #Your code starts HERE
    def __str__(self) -> str:  # str()
        object_str = f"'{self.amount} {self.currency}'"
        return object_str
    def __int__(self) -> int:
        object_int = self.amount
        return object_int
    def __repr__(self) -> str:
        object_repr = f"'{self.amount} {self.currency}'"
        return object_repr
    def __add__(self, other):
        if isinstance(other, (int, float)):  # Adding a numeric value
            return self.amount + other
        elif isinstance(other, Currency):  # Adding another Currency object
            if self.currency != other.currency:
                raise ValueError("Cannot add two different currencies.")
            return Currency(self.currency, self.amount + other.amount)
        else:
            raise TypeError("Unsupported operand type(s) for +: 'Currency' and '{}'".format(type(other).__name__))

    def __iadd__(self, other):
        if isinstance(other, (int, float)):  # Adding a numeric value
            self.amount += other
        elif isinstance(other, Currency):  # Adding another Currency object
            if self.currency != other.currency:
                raise ValueError(f"Cannot add between {self.currency} and {other.currency}.")
            self.amount += other.amount
        else:
            raise TypeError("Unsupported operand type(s) for +: 'Currency' and '{}'".format(type(other).__name__))
        return self

def main():   
    c1 = Currency('dollar', 5)
    c2 = Currency('dollar', 10)
    c3 = Currency('shekel', 1)
    c4 = Currency('shekel', 10)
    print(str(c1))
    print(int(c1))
    print(repr(c1))
    print(c1 + 5)
    print(c1 + c2)
    print(c1)
    c1 += 5
    print(c1)
    c1 += c2
    print(c1)
    #c1 += c3
if __name__ in "__main__":
    main()
"""
Using the code above, implement the relevant methods and dunder methods which will output the results below.
Hint : When adding 2 currencies which don’t share the same label you should raise an error.
>>> c1 = Currency('dollar', 5)
>>> c2 = Currency('dollar', 10)
>>> c3 = Currency('shekel', 1)
>>> c4 = Currency('shekel', 10)
>>> str(c1)
'5 dollars'
>>> int(c1)
5
>>> repr(c1)
'5 dollars'
>>> c1 + 5
10
>>> c1 + c2
15
>>> c1 
5 dollars
>>> c1 += 5
>>> c1
10 dollars
>>> c1 += c2
>>> c1
20 dollars
>>> c1 + c3
TypeError: Cannot add between Currency type <dollar> and <shekel>"""

#Exercise 2: Import
"""
In a file named func.py create a function that adds 2 number, and prints the result
In a file namedexercise_one.py import and the function
Hint: You can use the the following syntaxes:

import module_name 

OR 

from module_name import function_name 

OR 

from module_name import function_name as fn 

OR

import module_name as mn"""

# func.py and exercise_one.py



#Exercise 3: String Module

"""Generate random String of length 5
Note: String must be the combination of the UPPER case and lower case letters only. No numbers and a special symbol.
Hint: use the string module"""

import random
import string
letters = string.ascii_letters
random_string = ""
for i in range(5):
    random_string += random.choice(letters)
print(random_string)

#Exercise 4 : Current Date

"""Create a function that displays the current date.
Hint : Use the datetime module."""

import datetime
def current_date():
    print(datetime.date.today())

current_date()

#Exercise 5 : Amount Of Time Left Until January 1st

"""Create a function that displays the amount of time left from now until January 1st.
(Example: the 1st of January is in 10 days and 10:34:01hours)."""

def from_now_until_1jan():
    time_difference = datetime.datetime(2025,1,1,0,00) - datetime.datetime.now()
    days = time_difference.days
    seconds = time_difference.seconds
    
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60
    
    if days == 1:
        day_str = "day"
    else:
        day_str = "days"
    
    time_left_str = f"the 1st of January is in {days} {day_str} and {hours:02}:{minutes:02}:{seconds:02} hours."
    
    print(time_left_str)

from_now_until_1jan()
#Exercise 6 : Birthday And Minutes
from datetime import datetime
"""Create a function that accepts a birthdate as an argument (in the format of your choice), 
then displays a message stating how many minutes the user lived in his life."""
def minutes_in_life(birthdate_str):
    birthdate = datetime.strptime(birthdate_str, "%d/%m/%Y")
    time_difference = datetime.now() - birthdate
    minutes_lived = time_difference.total_seconds() // 60
    print(f"You have lived for {int(minutes_lived)} minutes.")

minutes_in_life("21/03/1999")


#Exercise 7 : Faker Module

"""Install the faker module, and take a look at the documentation and learn how to properly implement faker in your code.
Create an empty list called users. Tip: It should be a list of dictionaries.
Create a function that adds new dictionaries to the users list. Each user has the following keys: name, adress, langage_code. 
Use faker to populate them with fake data."""
from faker import Faker
fake = Faker()
users = []
def add_user():
    user = {
        'name': fake.name(),
        'address': fake.address(),
        'language_code': fake.language_code()
    }
    users.append(user)
for _ in range(5):
    add_user()

for user in users:
    print(user)
