import math 

def polysum (n, s):
    area = (0.25*n*s**2)/(math.tan(math.pi/n))
    perimeter_sqr = (s*n)**2
    return area + perimeter_sqr

print (polysum (n=6, s=2))