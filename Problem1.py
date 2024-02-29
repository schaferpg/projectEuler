# Problem 1: Multiples of 3 or 5
# https://projecteuler.net/problem=1

def multiples(num, ceiling):
    total = 0
    amount = ceiling//num
    for x in range(1 ,amount+1):
        total += num*x
    return total

ceiling = 1000
num1 = 3
num2 = 5

total = multiples(3,ceiling)+multiples(num2, ceiling) - multiples((num1*num2),ceiling)-ceiling

print(total)
