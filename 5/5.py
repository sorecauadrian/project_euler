def smallest_multiple(givenNumber : int):
  smallestMultiple = 1
  for i in range(1, givenNumber):
    smallestMultipleSoFar = smallestMultiple
    while smallestMultiple  % i != 0:
      smallestMultiple += smallestMultipleSoFar
  return smallestMultiple

if __name__ == '__main__':
  print(smallest_multiple(20))