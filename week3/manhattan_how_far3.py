import sys

def h(start, goal):
    assert "".join(sorted(start)) == " 12345678" and "".join(sorted(goal)) == " 12345678"
    if start == goal:
        return 0
    i = 0
    totalOutOfPlace = 0
    while i < len(start):
        if start[i] != goal[i] and start[i] != " ":
            totalOutOfPlace += move_calc(i, goal.index(start[i]))
        i +=1

    return totalOutOfPlace 

    
def move_calc(start, goal):
    row = abs((start % 3) - (goal % 3))
    column = abs((start // 3)-(goal //3))
    return row + column


if __name__=="__main__":
    print(h(sys.argv[1], sys.argv[2]))