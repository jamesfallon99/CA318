def h(start, goal):
    assert "".join(sorted(start)) == " 12345678" and "".join(sorted(goal)) == " 12345678"
    
    # Work out the manhattah distance of each tile from its eventual goal
    manhattan_distance = 0
    if start == goal:
        return manhattan_distance
    else:
        i = 0
        while i < len(start):
            if start[i] != goal[i] and start[i] != " ":
                row = abs((i % 3) - (goal.index(start[i]) % 3))
                column = abs((i // 3) - (goal.index(start[i]) // 3))
                manhattan_distance += row + column
            i += 1
        return manhattan_distance
print(h("1 3824756", "1238 4756"))

#On stackoverflow.com, I found a good formula that helped to solve the manhattan distance question
    #row = abs((i % 3) - (goal.index(start[i]) % 3))
    #column = abs((i // 3) - (goal.index(start[i]) // 3))
    #Decided to re-write my code for this question locally with this formula and got a working solution