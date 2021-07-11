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


def is_common_subsequence(sub, first, second): # if sub is a common subsequence of the two other strings
    check_first = is_subsequence(sub, first)
    check_second = is_subsequence(sub, second)

    if check_first and check_second == True:
        return True
    else:
        return False

print(is_common_subsequence("cat", "catd", "xtfy"))