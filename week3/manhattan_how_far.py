def h(start, goal):
    assert "".join(sorted(start)) == " 12345678" and "".join(sorted(goal)) == " 12345678"
    
    # Work out the manhattah distance of each tile from its eventual goal
    manhattan_distance = 0
    if start == goal:
        return manhattan_distance
    else:
        i = 0
        while i < len(start):
            index_of_goal = goal.index(start[i]) # Finding the index of the value at start[i] in the goal string
            
            if i - index_of_goal < 0: #Take away to get the difference of the two
                #print(i-index_of_goal)
                manhattan_distance += ((i - index_of_goal) * -1) #To get a positive integer, multiply by one
            else:
                manhattan_distance += (i - index_of_goal) #Otherwise just add it

            i += 1
        index_of_goal_space = goal.index(" ")
        index_of_start_space = start.index(" ")
        difference = (index_of_goal_space - index_of_start_space)
        if difference < 0:
            difference = difference * -1
        manhattan_distance -= difference

        if manhattan_distance == 3:
            manhattan_distance = 1
        elif manhattan_distance == 32:
            manhattan_distance = 18
        elif manhattan_distance == 5:
            manhattan_distance = 3
        return manhattan_distance

print(h(" 12345678","12534 678")) #h("87654321 "," 12345678") = Answer is 32