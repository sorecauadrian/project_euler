def get_numbers(file_name : str = "input_file.txt"):
  return open(file_name, "r").readlines()

def first_ten_digits_of_the_sum(numbers : list):
  sum = 0
  for number in numbers:
    sum += int(number)
  while sum >= 10000000000:
    sum //= 10
  return sum

if __name__ == "__main__":
  print(first_ten_digits_of_the_sum(get_numbers()))
