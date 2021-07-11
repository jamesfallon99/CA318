#In this recursive version of the problem, the memo should have len(s) rows and len(t) columns. There is no need to add the base case to the memo.When you run this code with the input s = XMJYAUZ and t = MZJAWXU
	 #[4, 3, 3, 2, 2, 2, 1]
	  #[4, 3, 3, 2, 1, 1, 1]
	 #[3, 3, 3, 2, 1, 1, 1]
	# [2, 2, 2, 2, 1, 1, 1]
	 #[2, 2, 2, 2, 1, 1, 1]
	 #[1, 1, 1, 1, 1, 1, 1]
	 #[1, 1, 0, 0, 0, 0, 0]
#The 4 in the upper left indicates that when s_index and t_index are both zero,
# then the longest common subsequence has length 4. As you move along the top row, you see the lengths of the subsequence as you move along the string t, namely, ZJAWXU, JAWXU, AWXU etc. 
# In this way, the memo contains the solutions to all the sub problems.

def recursive_lcs(s, s_index, t, t_index, memo):
    # Insert your code here
    if s_index == len(s) or t_index == len(t):
        return 0

    else:
        if memo[s_index][t_index] != -1:
            return memo[s_index][t_index] #If the value is already in the memo there's no point going through the calculations again so we just return the value instead
        else:
      # There are three possible moves from here ... move both, move s, move t.
      # Note that if s[s_index] == t[t_index], then we move both along (can't count either twice).
            move_both = recursive_lcs(s, s_index+1, t, t_index+1, memo) + 1 if s[s_index] == t[t_index] else 0
            move_s = recursive_lcs(s, s_index+1, t, t_index, memo)
            move_t = recursive_lcs(s, s_index, t, t_index + 1, memo)
            
            memo[s_index][t_index] = max([move_both, move_s, move_t])
            return  memo[s_index][t_index]
    
def longest_common_subsequence(s, t):
    # Create an appropriately sized memo
    # Initialised to -1
    memo = [ [-1 for i in range(len(t))] for j in range(len(s))]
    
    # Call the recursive function ... it will build up the memo.
    lcs = recursive_lcs(s, 0, t, 0, memo)
    
    return memo # now, return the memo

print(longest_common_subsequence("XMJYAUZ", "MZJAWXU"))