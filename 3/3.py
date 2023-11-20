def largest_prime_number(givenNumber):
  largestPrimeNumber = 0

  pseudoPrimeNumber = 2
  while givenNumber % pseudoPrimeNumber == 0:
    givenNumber /= pseudoPrimeNumber
    largestPrimeNumber = pseudoPrimeNumber

  pseudoPrimeNumber = 3
  while pseudoPrimeNumber <= givenNumber:
    while givenNumber % pseudoPrimeNumber == 0:
      givenNumber /= pseudoPrimeNumber
      largestPrimeNumber = pseudoPrimeNumber
    pseudoPrimeNumber += 2
  
  return largestPrimeNumber
    
if __name__ == '__main__':
  print(largest_prime_number(600851475143))