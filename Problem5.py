# Problem 5
# https://projecteuler.net/problem=5

# 1,3,5,7,9

start = 10
answer = 0


# Size of nums
num = 20


def smallestMultiple(num):
    primes = 3*5*7*11*13*17*19
    answer = 0
    arr = []
    
    for i in range(num,1,-1):
        arr.append(i)
    for i in range(30):
        i+=1
        tempNum = primes*2*i
        checker = True
        
        for a in arr:
            if(tempNum % a == 0):
                continue
            else:
                checker = False
                break

        if (checker == True):
            return(tempNum, i)
        


print(smallestMultiple(num))

            
