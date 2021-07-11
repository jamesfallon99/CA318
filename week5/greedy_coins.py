def make_sum(total, coins):
    # Total is the sum that you have to make and the coins list contains the values of the coins.
    # The coins will be sorted in descending order.
    
    # Place your code here
    i = 0
    count = 0
    coins_used = [] # a list indicating which coins are used to make the sum.
    amount = [0 for coin in coins] #Fill this list up with zeros to be able to add to it later
    while i < len(coins):
        while count + coins[i] <= total: #Make sure when you add the coin to count it is still less than the total
            count += coins[i]
            coins_used.append(coins[i]) #Append the coin used to the list
        i += 1

    j = 0
    for original_coin in coins:
        for used_coin in coins_used:
            if original_coin == used_coin:
                amount[j] += 1
        j += 1
    
    return amount

print(make_sum(43, [48, 24, 21, 1]))