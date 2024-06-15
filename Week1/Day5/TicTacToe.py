moves = {'11': "   ", "12": "   ", "13": "   ", "21": "   ", "22": "   ", "23": "   ", "31": "   ", "32": "   ", "33": "   "}
def display_board(moves):
    print("Welcome to TIC TAC TOE!")
    i = 0
    while i < 7:
        if i == 0:
            print("*" * 15)
        elif i == 1:
            print('*' + " " + moves['11'] + "|" + moves['12'] + "|" + moves['13'] + " " + "*")
        elif i == 2:
            print('*' + " " + "- -" + "|" + "- -"  + "|" + "- -"  + " " + "*")
        elif i == 3:
            print('*' + " " + moves["21"] + "|" + moves["22"] + "|" + moves["23"] + " " + "*")
        elif i == 4:
            print('*' + " " + "- -" + "|" + "- -"  + "|" + "- -"  + " " + "*")
        elif i == 5:
            print('*' + " " + moves["31"] + "|" + moves["32"] + "|" + moves["33"] + " " + "*")
        elif i == 6:
            print("*" * 15)
        print(' ')

        i+=1
display_board(moves)

def check_win(player):
    win_conditions = [
        ('11', '12', '13'),
        ('21', '22', '23'),
        ('31', '32', '33'),
        ('11', '21', '31'),
        ('12', '22', '32'),
        ('13', '23', '33'),
        ('11', '22', '33'),
        ('13', '22', '31')
    ]
    for condition in win_conditions:
        if moves[condition[0]] == moves[condition[1]] == moves[condition[2]] and moves[condition[0]] != "   ":
            print(f'{player}, You win!')
            exit()


def get_player_move(player):
    move = input(f"Player {player}, enter your move row and column together \n (e.g., '21' for row 2, column 1) or 'break' to stop: ")
    if move == 'break':
        exit()
    if move not in moves:
        print("Invalid input. Please enter a valid move.")
        return get_player_move(player)
    elif moves[move] != "   ":
        print("Not allowed. The position is already taken.")
        return get_player_move(player)     
    else:
        return move

def player_input():
    for i in range(len(moves)):
        if i % 2 == 0:
            player = "X"
            print("Player X's turn...")
        else:
            player = "O"
            print("Player O's turn...")
        
        move = get_player_move(player)
        moves[move] = f" {player} "
        display_board(moves)
        check_win(player)
    print("Tie!")
player_input()



