from puzzle8node import Puzzle8Node

def bfs(start, goal):
   # We will start here, so the list of nodes to do is the start
   todo = [start]
   visited = []
   num_searches = 0
   while len(todo) > 0:
      next = todo.pop(0) # Get (and remove) first element in the list (using the list as a queue)
      num_searches += 1

      if next == goal:
         return num_searches, next
      else:
         # Keep searching.
         visited.append(next) # Remember that we've been here
         children = list(child for child in next.get_children() if child not in visited and child not in todo)
         todo += children
   return num_searches, None # no route to goal, just return how long it took.
print(bfs(Puzzle8Node("1238 4765"),Puzzle8Node("87324 615")))