def sumOfDigitsOfFactorial(number: int):
    array_number = [1]
    for n in range(1, number + 1):
        carry = 0
        for i in range(len(array_number)):
            multiplyResult = array_number[i] * n + carry
            array_number[i] = multiplyResult % 10
            carry = multiplyResult // 10
        while carry:
            array_number.append(carry % 10)
            carry = carry // 10
    return sum(array_number)


if __name__ == '__main__':
    print(sumOfDigitsOfFactorial(100))

