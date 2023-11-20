def is_prime(givenNumber : int):
  if givenNumber < 2:
    return False
  if givenNumber > 2 and givenNumber % 2 == 0:
    return False
  for i in range(3, givenNumber, 2):
    if givenNumber % i == 0:
      return False
  return True

def prime_number(order : int):
  if order == 1:
    return 2
  else: 
    order -= 1
    i = 1
    while order != 0:
      i += 2
      if is_prime(i):
        order -= 1
  return i

if __name__ == '__main__':
  print(prime_number(10001))
