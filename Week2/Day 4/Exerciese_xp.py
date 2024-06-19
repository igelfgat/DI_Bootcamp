#Exercise 1 – Random Sentence Generator

# Description: In this exercise we will create a random sentence generator. 
#We will do this by asking the user how long the sentence should be and then printing the generated sentence.

# Hint : The generated sentences do not have to make sense.

# Create a function called get_words_from_file. This function should read the file’s content and return the words as a collection. 
#What is the correct data type to store the words?


# Create another function called get_random_sentence which takes a single parameter called length. 
#The length parameter will be used to determine how many words the sentence should have. The function should:
# use the words list to get your random words.
# the amount of words should be the value of the length parameter.
# Take the random words and create a sentence (using a python method), the sentence should be lower case.


import random
def get_words_from_file(file_location):
    with open(file_location) as file:
        contents = file.read().split()
    return contents

words_list = []
def get_random_sentence(length: int):
    global words_list
    if length > len(words_list):
        raise ValueError("Sample larger than population or is negative")
    random_words = random.sample(words_list, length)
    sentence = ' '.join(random_words).lower()
    return sentence

# Create a function called main which will:
    # Print a message explaining what the program does.

# Ask the user how long they want the sentence to be. Acceptable values are: an integer between 2 and 20. Validate your data and test your validation!
# If the user inputs incorrect data, print an error message and end the program.
# If the user inputs correct data, run your code.

"""def main():
    global words_list
    print("This program generates a random sentence from a list of words.")
    print("You can specify the length of the sentence you want to generate.")
    while True:
        try:
            length = int(input("Enter the length (between 2 and 20) of the sentence: "))
            if length <= 1 or length > 20:
                print("Please integer between 2 and 20.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter an integer.")
    file_location = "Week2/Day 4/words.txt"
    words_list = get_words_from_file(file_location)
    print(get_random_sentence(length))

if __name__ == "__main__":
    main()"""



#Exercise 2: Working With JSON

import json
sampleJson = """{ 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payable":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
}"""


"""Access the nested “salary” key from the JSON-string above.
Add a key called “birth_date” to the JSON-string at the same level as the “name” key.
Save the dictionary as JSON to a file."""

# Reading a json string

contents_dict = json.loads(sampleJson)  # json.loads reads a json string
print(contents_dict["company"]["employee"]["payable"]["salary"])
contents_dict["company"]["employee"]["birth_date"] = "1999-03-21"
print(contents_dict["company"]["employee"])
new_json_file_location = "Week2/Day 4/new_data.json"
print(contents_dict)

with open(new_json_file_location, mode="w") as file:
    json.dump(contents_dict, file)