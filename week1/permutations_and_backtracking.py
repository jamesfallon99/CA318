#
#  Back tracking version
#
#  Helps to have variables with global scope.
#
total = 0

letters = [] # This list will be updated by the recursive backtracking function (DFS)

def permutation(pos, next_letter, remaining_letters):
   global letters
   global total
   
   letters[pos] = next_letter # update the letters array

   if len(remaining_letters) == 0:  # no more letters => reached the end
      print("".join(letters), total) # ...  => found a new permutation
      # update the total

      total += 1
   else:
      # So, try each of the remaining letters in the next position
      for letter in remaining_letters:
         permutation(pos+1, letter, remaining_letters.replace(letter, ""))

   # When we are finished the recursive call, we revert to previous state
   letters[pos] = ' ' # actually doesn't matter in this case, because it will be overwritten when going forward. 

def main():
   global letters

   # Try a word
   word = 'jcdhfebiag'
   letters = ['-'] * len(word)
   for letter in word:
       remaining_letters = word.replace(letter, "") # find the remaining letters
       permutation(0, letter, remaining_letters) # let our function know which letters remain.
    

main()