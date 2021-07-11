import math
import random
#import optimization
from random import randint

def random_optimize(space, cost, steps=1000):
   # Get a random solution
   random_sol = [randint(space[i].minimum, space[i].maximum) for i in range(len(space))]
   best_so_far = random_sol
   for j in range(1, steps):

      # Create a random solution
      random_sol = [randint(space[i].minimum, space[i].maximum) for i in range(len(space))]
      # is this better than our best so far
      if cost(random_sol) < cost(best_so_far):
         print(j)#the only thing changed to this program
         best_so_far = random_sol
   return best_so_far


class DimensionRange():
   def __init__(self, mini, maxi):
      self.minimum = mini
      self.maximum = maxi

   def __str__(self):
      return "({}, {})".format(self.minimum, self.maximum)

   def __repr__(self):
      return str(self)

def cost(sol):
   error = 81 - sol[0] ** 2
   return error ** 2 # Square the error ensures it is always positive.

def main(args):
   if len(args) >= 2:
      num_steps = int(sys.argv[-1])
   else:
      num_steps = 1000

   random.seed(76)

   # Wanna get the square root of 81. Easy problem but used here
   #   to test the random_optimse algorithm.
   # First, assume that the solution is between 1 and 81.
   space = [DimensionRange(1, 81)] # Just one dimension in the range 1 to 81.
   print(space)

   sol = random_optimize(space, cost, num_steps)
   print("Solution is {}, the cost is {}".format(sol, cost(sol)))

import sys
main(sys.argv)

#remove this bit to get it to run
#take last value for j and plus 1
#
#   What is the smallest value that steps should be in order to find the solution
#   This answer will depend on the seed. You should submit None to get your seed value.
#
def sol():
   return 31 # for example.
   #Your seed is 76. You need to use this in the random.seed() call.