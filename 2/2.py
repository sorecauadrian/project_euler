def sum_of_even_numbers_in_fibonacci_sequence(limit : int):
  sum = 0
  first_term = 0
  second_term = 1
  while first_term + second_term < limit:
    third_term = first_term + second_term
    if third_term % 2 == 0:
      sum += third_term
    first_term = second_term
    second_term = third_term
  return sum

if __name__ == '__main__':
  print(sum_of_even_numbers_in_fibonacci_sequence(4000000))