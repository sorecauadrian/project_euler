from math import sqrt

def erathosthenes(n : int):
  array = [True for i in range(0, n)]
  for i in range(2, int(sqrt(n)) + 1):
    if array[i]:
      for j in range(i * i, n, i):
        array[j] = False
  s = 0
  for i in range(2, n):
    if array[i]:
      s += i
  return s

if __name__ == "__main__":
  print(erathosthenes(2000000))
  print(erathosthenes(10))