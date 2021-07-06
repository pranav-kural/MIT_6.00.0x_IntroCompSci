"""
myLog - return the largest power of b, such that b to that power is still less than or equal to x

"""
def myLog(x, b):
    '''a
    x: a positive integer
    b: a positive integer; b >= 2

    returns: log_b(x), or, the logarithm of x relative to a base b.
    '''
    power = 1
    while b ** power <= x:
      power += 1
    return power-1


print("log 16(2):", myLog(2, 2))