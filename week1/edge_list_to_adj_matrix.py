def make_adjacency_matrix(edge):
    #this function create an edge list representation of a graph using the supplied adjacency matrix

    # Maybe start with an empty edge_list
    adj = []
    # Insert code here
    i = 0
    k = 0
    while i < len(edge):
        adj.append([])
        while k < len(edge):
            if chr(ord("A") + k) in edge[i]:
                adj[i].append(1)
            else:
                adj[i].append(0)
            k += 1
        k = 0
        i += 1
    return adj

make_adjacency_matrix([['B', 'C'], ['A'], ['A']])

