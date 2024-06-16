#Challenge 1 : Sorting

"""Instructions

Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically.
Use List Comprehension
Example:

Suppose the following input is supplied to the program: without,hello,bag,world
Then, the output should be: bag,hello,without,world"""

#input_str = input("Enter comma separated sequence of words: ")
input_str = 'without,hello,bag,world'
sorted_str = ''
for word in sorted(input_str.split(',')):
    sorted_str += word
    sorted_str += ","
sorted_str = sorted_str[:-1] # Remove last comma
print(sorted_str)


#Challenge 2 : Longest Word

"""Instructions

Write a function that finds the longest word in a sentence. If two or more words are found, return the first longest word.
Characters such as apostrophe, comma, period count as part of the word (e.g. O’Connor is 8 characters long).
Examples

longest_word("Margaret's toy is a pretty doll.") ➞ "Margaret's"

longest_word("A thing of beauty is a joy forever.") ➞ "forever."

longest_word("Forgetfulness is by all means powerless!") ➞ "Forgetfulness"
"""

def the_longest_word(str):
    longest_word = ''
    for word in str.split():
        if word[-1] == "." or word[-1] == "!" or word[-1] == "?":
            word = word[:-1]
        if len(word) == len(longest_word):
            continue
        elif len(word) > len(longest_word):
            longest_word = word
    return(longest_word)
print(the_longest_word("A thing of beauty is a joy forever"))