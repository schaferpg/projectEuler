# Problem 6 - Sum Square Difference
# https://projecteuler.net/problem=6

def sumOfSquares(num):
    
    total = 0
    for i in range(1,num+1):
        total += pow(i,2)
    return total

def squaredSums(num):
    
    if (num % 2 == 0):
        num = ((num+1) * (num//2))
    else:
        num = num+1 * num//2 + num//2
    return(pow(num,2))


def diffenceOfSquares(num):
    return (squaredSums(num)-sumOfSquares(num))

num = 100

print (diffenceOfSquares(num))
