import math


def sumOfProperDivisors(number: int) -> int:
    sum = 1
    for divisor in range(2, int(math.sqrt(number) + 1)):
        if number % divisor == 0:
            sum += divisor
            if number // divisor > divisor:
                sum += number // divisor
    return sum


def sumOfAmicableNumbers(number: int) -> int:
    seen = set()
    for n in range(number + 1):
        sumOfProperDivisorsOfN = sumOfProperDivisors(n)
        if n == sumOfProperDivisors(sumOfProperDivisorsOfN) and n != sumOfProperDivisorsOfN:
            seen.add(sumOfProperDivisorsOfN)
            seen.add(n)
    return sum(seen)


if __name__ == '__main__':
    print(sumOfAmicableNumbers(10000))
