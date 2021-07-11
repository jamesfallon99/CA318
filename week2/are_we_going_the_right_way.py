def check_path(path):
    i = 0
    total = 0
    for child_node in range(len(path) -1):
        if path[i+1] in path[i].get_children():
            i += 1
            total += 1
    
    if total == len(path)-1:
        return True
    else:
        return False
    
