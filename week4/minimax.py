class Node:
   def __init__(self, v = -1, l=None, m=None, r=None):
      self.val = v
      self.left = l
      self.right = r
      self.mid = m

   def is_terminal(self):
      return self.left == None and self.mid == None and self.right == None

   def evaluation(self):
      return self.val

class Tree:
   def __init__(self):
      self.root = None

def minimax(tree):

    # return the value of the players node given the tree that contains the root node and all the descendants.
    # You can check whether a node is a terminal node by calling the is_terminal method.
    # These nodes have an evaluation.
    # You may use any resources that you discover as long as you acknowledge them.
    # return an integer value of the root