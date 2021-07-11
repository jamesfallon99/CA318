def find_number(amount, coins, memo):
   assert amount >= 0
   if amount in memo:
       return memo[amount]
   if amount == 0:
      return 0 # base case
   else:
      # Try every possibility
      memo[amount] = min([1 + find_number(amount - coin, coins, memo) for coin in coins if coin <= amount])
      return memo[amount]
#print(find_number(12, [5,2,1]))
def testing(amount, coins):
   memo = {}
   number_of_coins =  find_number(amount, coins, memo)
   return memo
   #return number_of_coins

print(testing(43, [48, 24, 21, 1]))