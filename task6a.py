#print(game_board)
def show():
    for row in game_board:
        for cell in row:
            print(cell, end=" ")
        print()

def check():
    if game_board[0][0] == "o" and game_board[0][1] == "o" and game_board[0][2] == "o":
        print("Player1 Wins!")
        return 1
    if game_board[1][0] == "o" and game_board[1][1] == "o" and game_board[1][2] == "o":
        print("Player1 Wins!")
        return 1
    if game_board[2][0] == "o" and game_board[2][1] == "o" and game_board[2][2] == "o":
        print("Player1 Wins!")
        return 1
    if game_board[0][0] == "o" and game_board[1][0] == "o" and game_board[2][0] == "o":
        print("Player1 Wins!")
        return 1
    if game_board[0][1] == "o" and game_board[1][1] == "o" and game_board[2][1] == "o":
        print("Player1 Wins!")
        return 1
    if game_board[0][2] == "o" and game_board[1][2] == "o" and game_board[2][2] == "o":
        print("Player1 Wins!")
        return 1
    if game_board[0][0] == "o" and game_board[1][1] == "o" and game_board[2][2] == "o":
        print("Player1 Wins!")
        return 1
    if game_board[2][0] == "o" and game_board[1][1] == "o" and game_board[0][2] == "o":
        print("Player1 Wins!")
        return 1

    if game_board[0][0] == "x" and game_board[0][1] == "x" and game_board[0][2] == "x":
        print("Player2 Wins!")
        return 1
    if game_board[1][0] == "x" and game_board[1][1] == "x" and game_board[1][2] == "x":
        print("Player2 Wins!")
        return 1
    if game_board[2][0] == "x" and game_board[2][1] == "x" and game_board[2][2] == "x":
        print("Player2 Wins!")
        return 1
    if game_board[0][0] == "x" and game_board[1][0] == "x" and game_board[2][0] == "x":
        print("Player2 Wins!")
        return 1
    if game_board[0][1] == "x" and game_board[1][1] == "x" and game_board[2][1] == "x":
        print("Player2 Wins!")
        return 1
    if game_board[0][2] == "x" and game_board[1][2] == "x" and game_board[2][2] == "x":
        print("Player2 Wins!")
        return 1
    if game_board[0][0] == "x" and game_board[1][1] == "x" and game_board[2][2] == "x":
        print("Player2 Wins!")
        return 1
    if game_board[2][0] == "x" and game_board[1][1] == "x" and game_board[0][2] == "x":
        print("Player2 Wins!")
        return 1

game_board = [["-","-","-"],
              ["-","-","-"],
              ["-","-","-"]]


show()

while True:
    
    print("Player 1")
    while True:
        row = int(input("Enter row:"))
        col = int(input("Enter col:"))
        if 0<=row<=2 and 0<=col<=2:
            if game_board[row][col] == "-":
                game_board[row][col] = "o"
                show()
                check()
                break
            else:
                print("ye khune dige entekhab kon!")
        else:
            print('beyne 0 , 2 entekhab kon!!!')

    if check() == 1:
        break


    if game_board[0][0] != "-" and game_board[0][1] != "-" and game_board[0][2] != "-" and game_board[1][0] != "-" and game_board[1][1] != "-" and game_board[1][2] != "-" and game_board[2][0] != "-" and game_board[2][1] != "-" and game_board[2][2] != "-" and check() != 1 :
        print("Player1 = Player2!")
        break

    
    print("Player 2")
    while True:
        row = int(input("Enter row:"))
        col = int(input("Enter col:"))
        if 0<=row<=2 and 0<=col<=2:
            if game_board[row][col] == "-":
                game_board[row][col] = "x"
                show()
                check()
                break
            else:
                print("ye khune dige entekhab kon!")
        else:
            print('beyne 0 , 2 entekhab kon!!!')

    if check() == 1:
        break

    if game_board[0][0] != "-" and game_board[0][1] != "-" and game_board[0][2] != "-" and game_board[1][0] != "-" and game_board[1][1] != "-" and game_board[1][2] != "-" and game_board[2][0] != "-" and game_board[2][1] != "-" and game_board[2][2] != "-" and check() != 1:
        print("Player1 = Player2!")
        break