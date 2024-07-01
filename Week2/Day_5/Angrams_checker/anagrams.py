from angram_checker import AnagramChecker
# This will contain all the UI (user interface) functionality of your program, and will rely on AnagramChecker for the anagram-related logic.

# 4. It should do the following:
#     4.1 Show a menu, offering the user to input a word or exit. Keep showing the menu until the user chooses to exit.
    # 4.2 If the user chooses to input a word, it must be accepted from the user’s keyboard input, and then be validated:
        #     Only a single word is allowed. If the user typed more than one word, show an error message. (Hint: how do we know how many words were typed?)
        #     Only alphabetic characters are allowed. No numbers or special characters.
        #     Whitespace should be removed from the start and end of the user’s input.
    # 4.3 Once your code has decided that the user’s input is valid, it should find out the following:
    #         All possible anagrams to the user’s word.
    #         Create an AnagramChecker instance and apply it to the steps created above.
    #         Display the information about the word in a user-friendly, nicely-formatted message such as:
    #                     YOUR WORD :”MEAT”
    #                     this is a valid English word.
    #                     Anagrams for your word: mate, tame, team.
def main():
    while True:    
        print("\nAnagram Checker")
        print("1. Input a word")
        print("2. Exit")
        choice = input("Choose an option: ")
        anagram_checker = AnagramChecker("Week2/Day_5/Angrams_checker/sowpods.txt")
        if choice == "1":
            word = input("Enter word: ").replace(" ", "") # without spaces before and after the word
            anagrams = anagram_checker.get_anagrams(word.upper())
            if anagrams:
                print(f"YOUR WORD : {word.upper()}")
                print("This is a valid English word.")
                print(f"Anagrams for your word: {', '.join(anagrams)}")
            else:
                print(f"No anagrams found for word: '{word}'.")
        elif choice == '2':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please choose again.")

if __name__ == "__main__":
    main()