#
#   In this exercise, find the most value you can get from items which you will fit into a knapsack
#    using dynamic programming.
#
#   return the memo that you create as a result
#
import math

class Item():
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight

def ks_greedy(initial_capacity, items):
    assert initial_capacity >= 0
    total_value = 0
    items.sort(key=item_value, reverse=True)#want to sort them into order(from highest to lowest) so that it can find the highest value first and check that to see if it's less than the initial capacity. If it is increase the total value, otherwise continue to the next item
    
    for item in items:
        while item.weight <= initial_capacity:
            total_value += item.value
            initial_capacity -= item.weight
    
    return total_value

def item_value(item):#helper function that will help sort the items into their correct order
    return item.value/item.weight



def dp_knapsack(initial_capacity, items):
   assert initial_capacity >= 0
   # Initialise memo to be - infinity for each of capacity + 1 values
   memo = [-math.inf] * (initial_capacity+1)    # Had a BUG here ... initially + infinity
   
   # Insert code here
   i = 0 #i will be every capacity value up to the initial capacity value. Therefore we can add in the total value for every value of i
   while i < len(memo):
       memo[i] = ks_greedy(i, items)
       i += 1
   
   return memo

#
#   normally, you would return memo[capacity] at this point, but in this exercise, you just return the memo.
#
#print(dp_knapsack(41, [Item(20,5), Item(200,11), Item(4,2)]))