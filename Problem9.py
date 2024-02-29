import math

# Brute Force
"""
for i in range(100,500):
    for j in range(1, 450):
        for k in range(1,450):
            if (k**2 + j**2 == i**2 and i+j+k == 1000):
                print(i*j*k)

"""

# Faster

for a in range(500,100,-1):
    for b in range(250,100,-1):
        c = 1000 - a - b
        if(b**2+c**2==a**2):
            print(a*b*c)
            print(a,b,c)
