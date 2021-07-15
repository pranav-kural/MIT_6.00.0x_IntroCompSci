def satisfiesF(L):
    """
    Assumes L is a list of strings
    Assume function f is already defined for you and it maps a string to a Boolean
    Mutates L such that it contains all of the strings, s, originally in L such
            that f(s) returns True, and no other elements. Remaining elements in L
            should be in the same order.
    Returns the length of L after mutation
    """
    currentLen = len(L)
    index = 0
    while index < currentLen:
      if not f(L[index]):
        L.pop(index)
        currentLen = len(L)
        continue
      index += 1
    
    return len(L)

def f(s):
    return 'a' in s
      
L = ['a', 'b', 'a']
print(satisfiesF(L))
print(L)

#run_satisfiesF(L, satisfiesF)