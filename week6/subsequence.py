#a subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.
def is_subsequence(s1,s2): 
    length_of_s1 = len(s1)
    length_of_s2 = len(s2)

    j = 0
    i = 0
    # Compare current character of s2 with first unmatched character of s1, If matched, then move ahead in s1 
      
    while j<length_of_s1 and i<length_of_s2: 
        if s1[j] == s2[i]:     
            j += 1    
        i +=1
          
    # If all characters of str1 matched, then j is equal to length of s1
    return j==length_of_s1

#print(isSubSequence("cat", "adtc"))