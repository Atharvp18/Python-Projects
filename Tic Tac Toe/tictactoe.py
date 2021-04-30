#The Tic Tac Toe game

theBoard={'7': ' ' , '8': ' ' , '9': ' ' ,
          '4': ' ' , '5': ' ' , '6': ' ' ,
          '1': ' ' , '2': ' ' , '3': ' ' }


BoardKeys=[]

for keys in theBoard:
    BoardKeys.append(keys)

def printBoard(board):
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('-----')

    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-----')

    print(board['1'] + '|' + board['2'] + '|' + board['3'])


def game():
    turn='X'
    count=0
    
    for i in range(10):
        printBoard(theBoard)
        print("It is the turn of "+turn+". Please specify the position you want to go. ")
        move=input()
        if theBoard[move]==' ':
            theBoard[move]= turn
            count+=1
        else:
            print("That place is filled up. Please specify another place.")
            continue

        if count>=5:
            if theBoard['7'] == theBoard['8'] == theBoard['9'] != ' ': # across the top
                printBoard(theBoard)
                print("\nGame Over.\n") 
                print("Player "+turn+" won the game.")                             
                break
            elif theBoard['4'] == theBoard['5'] == theBoard['6'] != ' ': # across the middle
                printBoard(theBoard)
                print("\nGame Over.\n") 
                print("Player "+turn+" won the game.")   
                break
            elif theBoard['1'] == theBoard['2'] == theBoard['3'] != ' ': # across the bottom
                printBoard(theBoard)
                print("\nGame Over.\n") 
                print("Player "+turn+" won the game.")   
                break
            elif theBoard['1'] == theBoard['4'] == theBoard['7'] != ' ': # down the left side
                printBoard(theBoard)
                print("\nGame Over.\n") 
                print("Player "+turn+" won the game.")   
                break
            elif theBoard['2'] == theBoard['5'] == theBoard['8'] != ' ': # down the middle
                printBoard(theBoard)
                print("\nGame Over.\n") 
                print("Player "+turn+" won the game.")   
                break
            elif theBoard['3'] == theBoard['6'] == theBoard['9'] != ' ': # down the right side
                printBoard(theBoard)
                print("\nGame Over.\n") 
                print("Player "+turn+" won the game.")   
                break 
            elif theBoard['7'] == theBoard['5'] == theBoard['3'] != ' ': # diagonal
                printBoard(theBoard)
                print("\nGame Over.\n") 
                print("Player "+turn+" won the game.")   
                break
            elif theBoard['1'] == theBoard['5'] == theBoard['9'] != ' ': # diagonal
                printBoard(theBoard)
                print("\nGame Over.\n") 
                print("Player "+turn+" won the game.")   
                break

        if turn =='X':
            turn = 'O'
        else:
            turn = 'X'    

        if count==9:
            print("\nGame Over.\n") 
            print("The game is a tie!")
            
    restart=input("Do you want to restart the game?(y/n)")

    if restart.lower()=='y':
        for values in theBoard:
            theBoard[values]=' '
        game()
    elif restart.lower()=='n':
        print("Thank you for playing!!") 
    else:
        print("Please reply with y or no")
        restart=input("Do you want to restart the game?(y/n)")
            
if __name__ == "__main__":
    game()
            
     

    





