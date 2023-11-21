def sum_of_digits(number:int, power:int):
    number_list = [1]
    carry = 0
    while power:
        for i in range(0, len(number_list)):
            multiplication_result = number_list[i] * number + carry
            carry = multiplication_result // 10
            number_list[i] = multiplication_result % 10
        while carry:
            number_list.append(carry % 10)
            carry = carry // 10
        power = power - 1
    sum = 0
    for element in number_list:
        sum += element
    return sum


if __name__ == "__main__":
    print(sum_of_digits(2, 1000))