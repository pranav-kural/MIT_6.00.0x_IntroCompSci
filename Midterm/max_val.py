def max_val(t): 
    """ t, tuple or list
        Each element of t is either an int, a tuple, or a list
        No tuple or list is empty
        Returns the maximum int in t or (recursively) in an element of t """
    if len(t) == 1:
      if isinstance(t[0], int):
        return max(t)
      elif isinstance(t[0][0], int):
        return max(t[0])
      else:
        return max_val(t[0])
    else:
      return max(max_val(t[:1]), max_val(t[1:]))


# test, should return: 5
print(max_val((5, (1,2), [[1],[2]])))

# max_val((5, (1,2), [[1],[9]])) returns 9