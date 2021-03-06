#
#   Use this class definition to work from.
#   This way of reading the dictionary is quete messy.
#   It is done this way to make testing easier.
#
from Node import Node
from string import ascii_lowercase
from read_dictionary import read_dictionary

valid_words = None

class WordGameNode(Node):
   def __init__(self, name, parent = None):
      # Ensure lowercase letters (no digits or special chars)
      for letter in name:
         assert letter in ascii_lowercase

      global valid_words
      if valid_words == None or len(valid_words) != len(name):
         # We only need to examine words which have the same length as our word (self.name)
         valid_words = read_dictionary("/etc/dictionaries-common/words", len(name))
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
                if new_word in valid_words:
                    child_words.append(WordGameNode(new_word))
        j += 1
        i = 0
      child_words.pop(0)
      return child_words

   def get_path(self):
      path = [self]
      child = self
      while child.get_parent() != None:
         child = child.get_parent()
         path.append(child)
      return path