def chain_length(number : int):
  if number <= 1:
    return 1
  if str(number) in chain_length_list.keys():
    return chain_length_list[str(number)]
  if number % 2:
    chain_length_list[str(number)] = chain_length(3 * number + 1) + 1
  else:
    chain_length_list[str(number)] = chain_length(number // 2) + 1
  return chain_length_list[str(number)]

if __name__ == "__main__":
  number = 0
  length = 0
  chain_length_list = {}
  for i in range(1000000):
    if chain_length(i) >= length:
      length = chain_length(i)
      number = i
  print(number)