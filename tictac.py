'''L = [1,2,3,4,5]

#print (L[0:3]) starts at location 0 but prints till 3 
print (L)
L[1] = 99'''




#tic tac toe game
game = [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],]

def game_board(player=0, row=0, column=0):

    print("  a   b   c")

    game[row][column] = player
    for count, row in enumerate(game):
        print(count, row)
   # for item in row:
    #    print(item)
game_board (player=1, row=2, column=1)

#game[0][1] = 1

#game_board ()
    
