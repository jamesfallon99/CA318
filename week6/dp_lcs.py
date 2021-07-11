def longest_common_subsequence(s, t):
    # Create an appropriately sized memo
    memo = [ [-1 for i in range(len(t) + 1)] for j in range(len(s) + 1)]
    # Set first row and first column to zero (represents a zero length string => 0 length lcs)
    # Row is s, col is t
    for row in range(len(s)+1):
        memo[row][0] = 0

    for col in range(len(t)+1):
        memo[0][col] = 0
    
    # Do the DP stuff here
    # for loops for s_index and t_index and build up the larger solutions from the smaller solutions.
    # Your code here.
    for i in range(len(s) + 1):
        for j in range(len(t) + 1):
            if i == 0 or j == 0:
                memo[i][j] = 0
            elif s[i-1] == t[j -1]:
                memo[i][j] = memo[i-1][j-1]+1
            else:
                memo[i][j] = max(memo[i-1][j], memo[i][j-1])

    #help from geeksforgeeks.org : https://www.geeksforgeeks.org/longest-common-subsequence-dp-4/
    
    # usually return memo[len(s)][len(t)] at this point, but for this exercise
    return memo
print(longest_common_subsequence("QWERTY", "WTYQRY"))