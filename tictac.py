game = [[0,0,0],[0,0,0],[0,0,0]]
def game_board(player,row,column):
    game[row][column] = player
    for row in game:
        print(row)

def win():
    for row in game:
        column_1 = row[0]
        column_2 = row[1] 
        column_3 = row[2]
        if column_1 == column_2 == column_3 != 0:
            print('Winner!')
            exit()
    for col in range(len(game[0])):
        check = []
        for row in game:
            check.append(row[col])
        if check.count(check[0]) == len(check) and check[0] != 0:
            print('Winner!')
            exit()
    else:
        pass
def main():
    print('Welcome to Tic Tac Toe Nav Edition\n')
    while(1):
        val = int(input("1.Play\n2.End Game\n>>>"))
        if (val==1):
            player=int(input('Enter Player:'))
            if(player==1 or player==2):
                row=int(input('Enter Row:'))
                column = int(input('Enter Column:'))
                print('Currently Playing:',player)
                game_board(player,row,column)
                win()
            else:
                print('Player Can Only Be 1 or 2')
                pass
        elif (val==2):
            exit()
        else:
            print('Wrong Value')
            pass

if __name__ == '__main__' :
    main()

