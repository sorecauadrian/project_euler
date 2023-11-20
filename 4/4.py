def verify_palindrome(givenNumber : int):
  return str(givenNumber) == str(givenNumber)[::-1]

def largest_palindrome_product(givenNumber : int):
  while givenNumber:
    if verify_palindrome(givenNumber):
      for i in range(999, 99, -1):
        quotient = givenNumber / i
        if quotient.is_integer():
          if quotient <= 999 and quotient >= 100:
            return givenNumber
    givenNumber -= 1
  return 0


if __name__ == '__main__':
  print(largest_palindrome_product(1000000))