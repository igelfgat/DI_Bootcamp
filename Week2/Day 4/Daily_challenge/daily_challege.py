#Daily Challenge : Text Analysis
#The goal of the exercise is to create a class that will help you analyze a specific text. 
#A text can be just a simple string, like “Today, is a happy day” or it can be an external text file.



"""
Part I

First, we will analyze a simple string, like “A good book would sometimes cost as much as a good house.”

Create a class called Text that takes a string as an argument and store the text in a attribute.
Hint: You need to manually copy-paste the text, straight into the code

Implement the following methods:
a method to return the frequency of a word in the text (assume words are separated by whitespace) return None or a meaningful message.
a method that returns the most common word in the text.
a method that returns a list of all the unique words in the text.

Part II

Then, we will analyze a text coming from an external text file. Download the_stranger.txt file.

Implement a classmethod that returns a Text instance but with a text file:

    >>> Text.from_file('the_stranger.txt')
Hint: You need to open and read the text from the text file.


Now, use the provided the_stranger.txt file and try using the class you created above."""

from collections import Counter
class Text:
    def __init__(self, txt_str:str)->object:
        self.txt_str = txt_str
        self.words = self.txt_str.split()

    def word_frequency(self):
        return Counter(self.words)
    
    def most_common_word(self):
        freq_counter = self.word_frequency()
        if not freq_counter:
            return "No words found in the text."

        max_freq = 0
        most_common_word = None

        for word, count in freq_counter.items():
            if count > max_freq:
                max_freq = count
                most_common_word = word

        return f"The most common word is '{most_common_word}' with {max_freq} occurrences."
    def unique_words(self):
        return list(self.word_frequency().keys())


    @classmethod  #classmethod
    def from_file(cls, file_name):
        with open(file_name, mode = 'r') as file:
            text_file = file.read()
            return cls(text_file)
            # return Text(text_file) : we are returning an object of Text
        
    def to_upper(self): #regular method justo to exemplify the difference
        return self.txt_str.upper()
    

text1 = Text('A good book would sometimes cost as much as a good house.')
freq_counter = text1.word_frequency()
print(freq_counter)
print(text1.most_common_word())
print(f"Unique words: {text1.unique_words()}")

print(text1.to_upper())
text2 = Text.from_file("Week2/Day 4/Daily_challenge/the_stranger.txt")