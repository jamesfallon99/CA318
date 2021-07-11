#
#   In this exercise, find the smallest number of coins to make up the specified amount
#    using dynamic programming.
#
#   return the memo that you create as a result
#
import math

def dp_make_change(amount, coins):
   assert amount >= 0
   # Initialise memo to be infinity for each of amount + 1 values
   memo = [math.inf] * (amount+1)
   
   # Insert code here
   memo[0] = 0
   for amount in range(1, len(memo)):
       for coin in coins:
        memo[amount] = min([memo[amount], memo[amount-coin] + 1])
   return memo

#
#   normally, you would return memo[amount] at this point, but in this exercise, you just return the memo.
#
print(dp_make_change(12, [5,2,1]))