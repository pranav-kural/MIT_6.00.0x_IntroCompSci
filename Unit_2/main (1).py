import math

def polysum(n,s):
  """
  Expects two arguments:
    n (type -> int/float): number of sides
    s (type -> int/float): length of each side
  Returns:
    sum of the area and the square of the perimeter (rounded to 4 decimal points)
  """
  area = (0.25*n*(s**2))/(math.tan(math.pi/n))
  perimeter = s * n
  return round(sum((area, perimeter**2)), 4)