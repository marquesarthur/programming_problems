
# @param a : list of integers
# @param b : integer
# @return a list of integers
def rotateArray(a, b):
    
    mod = b % len(a)
    ret = []
    
    for i in xrange(mod, len(a)):
        ret.append(a[i])
    for j in xrange(0, mod):
        ret.append(a[j])

    return ret

# Testing inputs/outputs
print rotateArray([1, 2, 3, 4, 5, 6], 1)
print rotateArray([14, 5, 14, 34, 42, 63, 17, 25, 39, 61, 97, 55, 33, 96, 62, 32, 98, 77, 35], 56)