#Write a function which takes three parameters, s, t and a memo which was constructed using the DP algorithm and return a valid longest common subsequence
#In previous questions we were finding the length of the lcs. This problem wants us to return the actual lcs
def longest_common_subsequence(s, t, memo):
     # insert your code here to traverse the memo and produce the lcs
     #Got help from geeksforgeeeks.org as after trial and error couldn't get my own solution working
     #https://www.geeksforgeeks.org/printing-longest-common-subsequence/
    length_of_s = len(s)
    length_of_t = len(t)
    index = memo[length_of_s][length_of_t]

    lcs = [""] * (index + 1)
    lcs[index] = ""

    # Start from the right-most-bottom-most corner and 
    # one by one store characters in lcs[] 

    i = length_of_s
    j = length_of_t

    while i > 0 and j > 0:# If current character in s[] and t are same, then 
                            # current character is part of LCS 
        if s[i -1] == t[j-1]:
            lcs[index-1] = s[i-1]
            i -= 1
            j -= 1
            index -= 1
        
        # If not same, then find the larger of two and 
        # go in the direction of larger value 
        elif memo[i-1][j] > memo[i][j-1]:
            i -= 1
        else:
            j -= 1
    lcs_string = "".join(lcs)
    return lcs_string

def length_of_lcs(s, t):
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
    
    # usually return memo[len(s)][len(t)] at this point, but for this exercise
    get_lcs = longest_common_subsequence(s, t, memo)
    print(get_lcs)

length_of_lcs("XMJYAUZ", "MZJAWXU")