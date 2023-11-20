def sum_of_squares(givenNumber : int):
  return givenNumber * (givenNumber + 1) * (2 * givenNumber + 1) / 6

def square_of_sum(givenNumber : int):
  return (givenNumber * (givenNumber + 1) / 2) ** 2

def difference(givenNumber : int):
  return square_of_sum(givenNumber) - sum_of_squares(givenNumber)

if __name__ == '__main__':
  print(int(difference(100)))