# 1.game.py – this file/module should contain a class called Game. It should have 4 methods:
#     1.1 get_user_item(self) – Ask the user to select an item (rock/paper/scissors). 
#      Keep asking until the user has selected one of the items – use data validation and looping. Return the item at the end of the function.

#     1.2 get_computer_item(self) – Select rock/paper/scissors at random for the computer. 
#        Return the item at the end of the function. Use python’s random.choice() function (read about it online).

#     1.3 get_game_result(self, user_item, computer_item) – Determine the result of the game.
#         Parameters:
#             user_item – the user’s chosen item (rock/paper/scissors)
#             computer_item – the computer’s chosen (random) item (rock/paper/scissors)
#             Return either win, draw, or loss. Where win means that the user has won, draw means the user and the computer got the same item, and loss means that the user has lost.
#     1.4 play(self) – the function that will be called from outside the class (ie. from rock-paper-scissors.py). It will do 3 things:
#         1.4.1 Get the user’s item (rock/paper/scissors) and remember it

#         1.4.2 Get a random item for the computer (rock/paper/scissors) and remember it

#         1.4.3 Determine the results of the game by comparing the user’s item and the computer’s item
#             - Print the output of the game; something like this: “You selected rock. The computer selected paper. You lose”, “You selected scissors. The computer selected scissors. You drew!”

#             - Return the results of the game as a string: win;draw;loss;, where win means that the user has won, draw means the user and the computer got the same item, and loss means that the user has lost.
import random
class Game:
    def get_user_item(self):
        while True:
            user_item = input("Enter rock/paper/scissors: ")
            if user_item == "rock" or user_item == "paper" or user_item == "scissors":
                return user_item
            else:
                print("Invalid choice. Please choose again.")

    def get_computer_item(self):
        computer_item = ['rock', 'paper', 'scissors']
        return random.choice(computer_item)

    def get_game_result(self, user_item, computer_item):
        #results = {"win":0, "draw":0, "loss":0}
        if user_item == computer_item:
            #results["draw"] = results["draw"] + 1
            return "draw"
        elif (user_item == 'rock' and computer_item == 'scissors') or \
             (user_item == 'paper' and computer_item == 'rock') or \
             (user_item == 'scissors' and computer_item == 'paper'):
            #results["win"] = results["win"] + 1
            return "win"
        else:
            #results["loss"] = results["loss"] + 1
            return "loss"
        
    def play(self):
        user_item = self.get_user_item()
        computer_item = self.get_computer_item()
        result = self.get_game_result(user_item, computer_item)

        print(f"You selected {user_item}. The computer selected {computer_item}. You {result}.")
        return result

