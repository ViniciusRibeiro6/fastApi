def find(array, fn):
  for elem in array:
    result = fn(elem)
    if result == True:
      return elem
    
  return None