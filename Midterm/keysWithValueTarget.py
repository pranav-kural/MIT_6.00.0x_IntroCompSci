def keysWithValue(aDict, target):
    '''
    aDict: a dictionary
    target: an integer
    '''
    return sorted(list({key:value for key, value in aDict.items() if value == target}.keys()))

# test 1: should return [1, 6, 9]
a = keysWithValue({1:3,4:1,5:2,6:3,7:0,9:3}, 3)

# test 2: should return [3, 9, 15]
a = keysWithValue({4:3,9:1,5:2,3:1,7:0,15:1}, 1)

print(a)