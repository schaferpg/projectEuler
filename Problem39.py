# Problem 39
# https://projecteuler.net/problem=39

"""

a^2 + b^2 = c^2
a + b + c = p

a + b - p = c

(a + b - p)^2 = c^2
a^2 + ab -ap + b^2 -bp + p^2 = c^2

a^2 + b^2 = c^2
a^2 + b^2 = a^2 + ab -ap + b^2 -bp + p^2

-ab + ap + bp = p^2

- ab + (ap+bp)
2(p(a + b) - ab) = p^2
"""

def solver(p):
    counter = 0
    for a in range(p//2):
        for b in range(p//2):
            if (pow(p,2) == 2*((p*(a + b) - a*b))):
                counter += 1
    return counter

def iterator(n):
    big_count = 0
    p = 0
    for i in range(n):
        temp_count = solver(i)
        if (temp_count > big_count):
            big_count = temp_count
            p = i
    return p
        
print(iterator(1000))
