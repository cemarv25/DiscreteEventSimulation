## Functions ##

def get_middle_digits(yn, D):
  """
  Function to get the middle digits of a string number.
  
  yn : str
    The string to get the middle digits from.
  D : int
    The qty of the middle digits.
  """
  spare = len(yn) - D
  if spare % 2 != 0:
    yn = "0" + yn
    spare = len(yn) - D

  left = int(spare / 2)
  right = len(yn) - left

  return yn[left:right]

## Exceptions ##

class NoMoreMiddleDigits(Exception):
    """The program is not able to get the middle digits"""
    pass