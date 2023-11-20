from math import sqrt

def number_of_divisors(x):
  sum = 0
  for i in range(1, int(sqrt(x))):
    if x % i == 0:
      sum += 2
      if x / i == i:
        sum -= 1
  return sum

def triangular_number_with_over_x_divisors(x : int = 500):
  i = 1
  while True:
    if number_of_divisors(i * (i + 1) / 2) > x:
      return i * (i + 1) / 2
    i += 1

if __name__ == "__main__":
  print(triangular_number_with_over_x_divisors(500))