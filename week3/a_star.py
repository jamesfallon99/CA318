from puzzle8node import Puzzle8Node

def a_star_search(start, goal):
   todo = [start]
   visited = set()
   num_searches = 0
   while len(todo) > 0:
      next = todo.pop(0) # Get (and remove) first element in the list (using the list as a queue)
      num_searches += 1

      if next == goal:
         return num_searches, next
      else:
         # Keep searching.
         visited.add(next) # Remember that we've been here

         # Add children to the todo list and update the score
         for child in next.get_children():
            if child not in visited and child not in todo:
               child.score = child.depth + child.heuristic(goal)  # score = g(n) + h(n)
               todo.append(child)

         # Sort the children by score (lowest better)
         todo.sort(key = lambda x : x.score)

   return num_searches, None # no route to goal

print(a_star_search(Puzzle8Node("1238 4765"), Puzzle8Node("87324 615")))
