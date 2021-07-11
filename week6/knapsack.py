#
#   In this exercise, find the most value the greedy algorithm finds
#
class Item():
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight

def ks_greedy(initial_capacity, items):
    assert initial_capacity >= 0
    total_value = 0
    items.sort(key=item_value, reverse=True)#want to sort them into order(from highest to lowest) so that it can find the highest value first and check that to see if it's less than the initial capacity. If it is increase the total value, otherwise continue to the next item
    #if initial_capacity == 0:
       #return 0
    #else:
        #options_to_choose = [item.value + ks_greedy(initial_capacity - item.weight, items) for item in items if item.weight <= initial_capacity]
        #if len(options_to_choose) == 0:
            #return 0
        #else:
            #return max(options_to_choose)
    for item in items:
        while item.weight <= initial_capacity:
            total_value += item.value
            initial_capacity -= item.weight
    
    return total_value

def item_value(item):#helper function that will help sort the items into their correct order
    return item.value/item.weight

print(ks_greedy(41, [Item(20,5), Item(200,11), Item(4,2)])) #Need to sort based off of highest value