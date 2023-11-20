def sum_of_multiplies_of_3_or_5(given_number):
  sum = 0
  for i in range(given_number):
    if i % 3 == 0 or i % 5 == 0:
      sum += i
  return sum

if __name__ == '__main__':
  print(sum_of_multiplies_of_3_or_5(1000))