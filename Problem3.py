# Problem 4
# https://projecteuler.net/problem=4



#import time
import time

t0 = time.time()



# Create largest palindrome number product holder
holderLargestPalidrome = 0
a = 0
b = 0
# Create palidrome method to check for palindrome
def palidrome(num):
    stringNum = str(num)
    for i in range(len(stringNum)//2):
        if (stringNum[i] == stringNum[len(stringNum)-i-1]):
            continue
        else:
            return 0
    return int(stringNum)

for x in range(100,1000):
    for y in range(100,1000):
        newNum = palidrome(x*y)
        if (holderLargestPalidrome < newNum):
            holderLargestPalidrome = newNum
            a = x
            b= y

print(holderLargestPalidrome)
print(a, b)
t1 = time.time()
total = t1-t0
print(total)
    
