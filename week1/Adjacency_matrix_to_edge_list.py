def make_edge_list(adjacency):
    #this function create an edge list representation of a graph using the supplied adjacency matrix

    # Maybe start with an empty edge_list
    edge_list = []
    # Insert code here
    i = 0
    k = 0
    while i < len(adjacency):
        edge_list.append([])
        while k < len(adjacency[i]):
            if adjacency[i][k] == 1:
                edge_list[i].append(chr(ord("A") + k))
            k += 1
        k = 0
        i += 1

    
    return edge_list


make_edge_list([[0, 1, 1],
[1, 0, 0],
[1, 0, 0]])
