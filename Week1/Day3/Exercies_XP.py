#Exercise 1 : Convert Lists Into Dictionaries

"""Instructions

Convert the two following lists, into dictionaries.
Hint: Use the zip method
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
Expected output:
{'Ten': 10, 'Twenty': 20, 'Thirty': 30}"""

"""keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

dict = {}
i = 0
while i < len(keys):
    dict[keys[i]] = values[i]
    i += 1
print(dict)"""


#Exercise 2 : Cinemax #2

"""Instructions

A movie theater charges different ticket prices depending on a person’s age.
if a person is under the age of 3, the ticket is free.
if they are between 3 and 12, the ticket is $10.
if they are over the age of 12, the ticket is $15.

Given the following object:

family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
How much does each family member have to pay ?

Print out the family’s total cost for the movies.
Bonus: Ask the user to input the names and ages instead of using the provided family variable 
(Hint: ask the user for names and ages and add them into a family dictionary that is initially empty)."""

"""family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
total_cost = 0

for key,value in family.items():
    if value < 3:
        print(key, "for free")
    elif 3 < value < 12:
        print(key, ":10$")
        total_cost += 10
    elif value > 12:
        print(key, ": 15$")
        total_cost += 15
print(total_cost)

#Bonus
family_dict = {}
total_cost = 0
while True:
    user_name = input("Enter your name or 'break' for quit: ")
    if user_name == "break":
        break 
    user_age = input("Enter your age or 'break' for quit: ")
    if user_age == "break":
        break 
    family_dict[user_name] = user_age

for key,value in family_dict.items():
    if int(value) < 3:
        print(key, "for free")
    elif 3 < int(value) < 12:
        print(key, ":10$")
        total_cost += 10
    elif int(value) > 12:
        print(key, ": 15$")
        total_cost += 15
print(total_cost)
print(family_dict)"""

#Exercise 3: Zara

"""Instructions

Here is some information about a brand.
name: Zara 
creation_date: 1975 
creator_name: Amancio Ortega Gaona 
type_of_clothes: men, women, children, home 
international_competitors: Gap, H&M, Benetton 
number_stores: 7000 
major_color: 
    France: blue, 
    Spain: red, 
    US: pink, green


2. Create a dictionary called brand which value is the information from part one (turn the info into keys and values).
The values type_of_clothes and international_competitors should be a list. The value of major_color should be a dictionary.
3. Change the number of stores to 2.
4. Print a sentence that explains who Zaras clients are.
5. Add a key called country_creation with a value of Spain.
6. Check if the key international_competitors is in the dictionary. If it is, add the store Desigual.
7. Delete the information about the date of creation.
8. Print the last international competitor.
9. Print the major clothes colors in the US.
10. Print the amount of key value pairs (ie. length of the dictionary).
11. Print the keys of the dictionary.
12. Create another dictionary called more_on_zara with the following details:

creation_date: 1975 
number_stores: 10 000


13. Use a method to add the information from the dictionary more_on_zara to the dictionary brand.
14. Print the value of the key number_stores. What just happened ?"""
    
"""store_info = {
    "name": "Zara",
    "creation_date": 1975,
    "creator_name": "Amancio Ortega Gaona",
    "type_of_clothes": ["men", "women", "children", "home"],
    "international_competitors": ["Gap", "H&M", "Benetton"],
    "number_stores": 7000,
    "major_color": {"France": ["blue"], "Spain": ["red"], "US": ["pink", "green"]},
}

store_info["number_stores"] = 2
print(f"Zaras clients are people who want to buy clother these types: {store_info['type_of_clothes']}")
store_info["country_creation"] = "Spain"
if store_info["international_competitors"]:
    store_info["international_competitors"].append("Desigual")
print(store_info)
store_info.pop('creation_date')
print(store_info["international_competitors"][-1])
print(store_info['major_color']["US"])
print(len(store_info))
for key in store_info:
    print(key)

more_on_zara = {
    "creation_date": 1975,
    "number_stores": 10000
}
store_info.update(more_on_zara)
print(store_info["number_stores"]) # The value of number stores was updated from 7000 to 10000"""

#Exercise 4 : Disney Characters

"""Instructions

Use this list :

users = ["Mickey","Minnie","Donald","Ariel","Pluto"]
Analyse these results :

#1/

>>> print(disney_users_A)
{"Mickey": 0, "Minnie": 1, "Donald": 2, "Ariel": 3, "Pluto": 4}

#2/

>>> print(disney_users_B)
{0: "Mickey",1: "Minnie", 2: "Donald", 3: "Ariel", 4: "Pluto"}

#3/ 

>>> print(disney_users_C)
{"Ariel": 0, "Donald": 1, "Mickey": 2, "Minnie": 3, "Pluto": 4}


Use a for loop to recreate the 1st result. Tip : don’t hardcode the numbers.
Use a for loop to recreate the 2nd result. Tip : don’t hardcode the numbers.
Use a method to recreate the 3rd result. Hint: The 3rd result is sorted alphabetically.
Only recreate the 1st result for:
The characters, which names contain the letter “i”.
The characters, which names start with the letter “m” or “p”."""

users = ["Mickey","Minnie","Donald","Ariel","Pluto"]
disney_users_A = {}
i = 0
for name in users:
    disney_users_A[name] = i
    i += 1

j=0
disney_users_B = {}
for name in users:
    disney_users_B[j] = name
    j += 1

k=0
disney_users_C = {}
users.sort()
for name in users:
    disney_users_C[name] = k
    k += 1
print(disney_users_C)

disney_users_A = {}
i = 0
for name in users:
    if "i" in name:
        disney_users_A[name] = i
    i += 1

disney_users_A = {}
i = 0
for name in users:
    if name[0] == "P" or name[0] == "M":
        disney_users_A[name] = i
    i += 1
print(disney_users_A)