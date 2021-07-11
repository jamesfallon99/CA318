def h(start, goal):
    # ensure that start and goal are valid positions
    assert "".join(sorted(start)) == " 12345678" and "".join(sorted(goal)) == " 12345678"
    
    # Work out how many tiles are out of place
    num_tiles_out_of_place = 0
    if start == goal:
        return num_tiles_out_of_place
    else:
        i = 0
        while i < len(start):
            if start[i] != goal[i]:
                num_tiles_out_of_place += 1
            i += 1
        return num_tiles_out_of_place -1

print(h(" 12345678"," 12345678"))