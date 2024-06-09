# Daily Challenge: Build Up A String
"""
Instructions

Using the input function, ask the user for a string. The string must be 10 characters long.
If it’s less than 10 characters, print a message which states “string not long enough”.
If it’s more than 10 characters, print a message which states “string too long”.
If it’s 10 characters, print a message which states “perfect string” and continue the exercise.

Then, print the first and last characters of the given text.

Using a for loop, construct the string character by character: Print the first character, then the second, then the third, until the full string is printed. For example:
The user enters "HelloWorld"
Then, you have to construct the string character by character
H
He
Hel
... etc
HelloWorld


4. Bonus: Swap some characters around then print the newly jumbled string (hint: look into the shuffle method). For example:
Hlrolelwod
"""
import random
user_string = input("Enter text with 10 characters: ")
if len(user_string) < 10:
    print("string not long enough")
elif len(user_string) > 10:
    print("string too long")
elif len(user_string) == 10:
    print("perfect string")

print("first character: ", user_string[0], "last character: ", user_string[-1])
result = []
for elem in user_string:
    result += elem
    print(result)
random.shuffle(result)
print("shuffled result", result)

