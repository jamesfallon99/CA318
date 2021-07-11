def sol():
    #  return the value of the players node given the nine terminal values
    # return None to receive your nine terminal values.
    # e.g. Your values are [24, 30, 25, 13, 20, 4, 27, 16, 19]
    
    return 24
    #player 1 will choose the largest in row 2. When these divide down in row three, the largest values
    #will be the ones resulting in player 1s turn.
    #Player 2 will then choose the smallest value amongst that list of numbers.
    #Therefore 24 is the actual value for player 1 once he continues.

    #player one chooses between 3 options.
    #player 2 then chooses between another 3 options depending on the option chosen by player 1.
    #player 1 will choose the max value
    #player 2 will choose the min value.



    #24 30 25   13 20 4   27 16 19
    #because player 1 chose the highest value in their turn
    #player 2 will then choose the lowest value out of the resulting values from player 1's turn.
    #this means player 2 will choose 24 and player 1 will have to continue from there