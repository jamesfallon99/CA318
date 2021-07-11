def get_lcss(s, s_index, t, t_index):
   if s_index == len(s) or t_index == len(t):
      return 0
   else:
      # There are three possible moves from here ... move both, move s, move t.
      # Note that if s[s_index] == t[t_index], then we move both along (can't count either twice).
      move_both = get_lcss(s, s_index+1, t, t_index+1) + 1 if s[s_index] == t[t_index] else 0
      move_s = get_lcss(s, s_index+1, t, t_index)
      move_t = get_lcss(s, s_index, t, t_index + 1)

      # Return the largest of the three moves
      return max([move_both, move_s, move_t])

def main(args):
   if len(args) < 2:
      print("Usage: lcss s t")
   else:
      s = args[1]
      t = args[2]

      lcss = get_lcss(s, 0, t, 0)
      print(lcss)

import sys
if __name__ == "__main__":
   main(sys.argv)