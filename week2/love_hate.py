from Node import Node
from string import ascii_lowercase

class WordGameNode(Node):
   def __init__(self, name, parent = None):
      # Ensure lowercase letters (no digits or special chars)
      for letter in name:
         assert letter in ascii_lowercase
      self.name = name
      self.parent = parent

   def __str__(self):
      return self.name

   def get_children(self):
      # all one letter mutations of the word
      letters = "abcdefghijklmnopqrstuvwxyz"
      child_words = []
      child_words.append(self.name)
      i = 0
      j = 0
      while j < len(self.name):
        while i < len(letters):
            new_word = child_words[0].replace(child_words[0][j], letters[i])
            i += 1
            if new_word != self.name:
                child_words.append(WordGameNode(new_word))
        j += 1
        i = 0
      child_words.pop(0) # To remove the initial word ie self.name from the list
      return child_words

   def get_path(self):
      # insert code here
      return path