import random
import unittest

# Create simulated tic tac toe game. The game should consist of 2 players, one using 'X' and the other 'O'. 
# After each turn, player should mark a space on the board according to their corresponding marker. 
# Once a player successfully gets 3 pieces across or diagonally, print who won. 
# If there is no winner, print 'Tie game'.
# Print the position of the newly placed marker after each turn
# Place game within in a function called tic tac toe

def ticTacToe():
    board = ['[-]', '[-]', '[-]'], ['[-]', '[-]', '[-]'], ['[-]', '[-]', '[-]']
    for row in board:
        print(row)
    print('---------------')
    p1Turn = True
    count = 0
    while True:
        while p1Turn == True:
            row = random.randint(0, 2)
            col = random.randint(0, 2)
            if board[row][col] == '[-]':
                board[row][col] = '[X]'
                for row in board:
                    print(row)
                print('---------------')
                p1Turn = False
                count += 1
        if count >= 5:
            if (board[0][0] == board[0][1] == board[0][2]) and board[0][0] != '[-]': # top row win
                if board[0][0] == '[X]':
                    print("Game Over.\nPlayer 1 wins.")
                else:
                    print("Game Over.\nPlayer 2 wins.")
                break
            elif (board[2][0] == board[2][1] == board[2][2]) and board[2][0] != '[-]': # bottom row win
                if board[2][0] == '[X]':
                    print("Game Over.\nPlayer 1 wins.")
                else:
                    print("Game Over.\nPlayer 2 wins.")
                break
            elif (board[1][0] == board[1][1] == board[1][2]) and board[1][0] != '[-]': # middle row win
                if board[1][0] == '[X]':
                    print("Game Over.\nPlayer 1 wins.")
                else:
                    print("Game Over.\nPlayer 2 wins.")
                break
            elif (board[0][0] == board[1][0] == board[2][0]) and board[0][0] != '[-]': # left column win
                if board[0][0] == '[X]':
                    print("Game Over.\nPlayer 1 wins.")
                else:
                    print("Game Over.\nPlayer 2 wins.")
                break
            elif (board[0][2] == board[1][2] == board[2][2]) and board[0][2] != '[-]': # right column win
                if board[0][2] == '[X]':
                    print("Game Over.\nPlayer 1 wins.")
                else:
                    print("Game Over.\nPlayer 2 wins.")
                break
            elif (board[0][1] == board[1][1] == board[2][1]) and board[0][1] != '[-]': # middle column win
                if board[0][1] == '[X]':
                    print("Game Over.\nPlayer 1 wins.")
                else:
                    print("Game Over.\nPlayer 2 wins.")
                break
            elif (board[0][0] == board[1][1] == board[2][2]) and board[0][0] != '[-]': # left down diagonal win
                if board[0][0] == '[X]':
                    print("Game Over.\nPlayer 1 wins.")
                else:
                    print("Game Over.\nPlayer 2 wins.")
                break
            elif (board[2][0] == board[1][1] == board[0][2]) and board[2][0] != '[-]': # left up diagonal win
                if board[2][0] == '[X]':
                    print("Game Over.\nPlayer 1 wins.")
                else:
                    print("Game Over.\nPlayer 2 wins.")
                break
            elif count >= 9:
                print("Game Over. Both Player Tied.")
                break
        
        while p1Turn == False:
            row = random.randint(0, 2)
            col = random.randint(0, 2)
            if board[row][col] == '[-]':
                board[row][col] = '[O]'
                for row in board:
                    print(row)
                print('---------------')
                p1Turn = True
                count += 1

        if count >= 5:
            if (board[0][0] == board[0][1] == board[0][2]) and board[0][0] != '[-]': # top row win
                if board[0][0] == '[X]':
                    print("Game Over.\nPlayer 1 wins.")
                else:
                    print("Game Over.\nPlayer 2 wins.")
                break
            elif (board[2][0] == board[2][1] == board[2][2]) and board[2][0] != '[-]': # bottom row win
                if board[2][0] == '[X]':
                    print("Game Over.\nPlayer 1 wins.")
                else:
                    print("Game Over.\nPlayer 2 wins.")
                break
            elif (board[1][0] == board[1][1] == board[1][2]) and board[1][0] != '[-]': # middle row win
                if board[1][0] == '[X]':
                    print("Game Over.\nPlayer 1 wins.")
                else:
                    print("Game Over.\nPlayer 2 wins.")
                break
            elif (board[0][0] == board[1][0] == board[2][0]) and board[0][0] != '[-]': # left column win
                if board[0][0] == '[X]':
                    print("Game Over.\nPlayer 1 wins.")
                else:
                    print("Game Over.\nPlayer 2 wins.")
                break
            elif (board[0][2] == board[1][2] == board[2][2]) and board[0][2] != '[-]': # right column win
                if board[0][2] == '[X]':
                    print("Game Over.\nPlayer 1 wins.")
                else:
                    print("Game Over.\nPlayer 2 wins.")
                break
            elif (board[0][1] == board[1][1] == board[2][1]) and board[0][1] != '[-]': # middle column win
                if board[0][1] == '[X]':
                    print("Game Over.\nPlayer 1 wins.")
                else:
                    print("Game Over.\nPlayer 2 wins.")
                break
            elif (board[0][0] == board[1][1] == board[2][2]) and board[0][0] != '[-]': # left down diagonal win
                if board[0][0] == '[X]':
                    print("Game Over.\nPlayer 1 wins.")
                else:
                    print("Game Over.\nPlayer 2 wins.")
                break
            elif (board[2][0] == board[1][1] == board[0][2]) and board[2][0] != '[-]': # left up diagonal win
                if board[2][0] == '[X]':
                    print("Game Over.\nPlayer 1 wins.")
                else:
                    print("Game Over.\nPlayer 2 wins.")
                break
            elif count >= 9:
                print("Game Over. Both Player Tied.")
                break

ticTacToe()

class TestTic(unittest.TestCase):
    def testTicTacToe(self):
        self.assertEqual()