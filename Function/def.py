# Python program to print first 10 prime numbers

# A function name prime is defined
# using def
def fun(n):
    x = 2
    count = 0
    while count < n:
        for d in range(2, int(x ** 0.5) + 1):
            print(range(2, int(x ** 0.5) + 1))
            print(x,"d is",d)  # check divisibility only up to sqrt(x)
            if x % d == 0:
                break  # if divisible, it's not prime, so break the loop
        else:
            print("prime",x)  # prime number
            count += 1
        x += 1

# Driver Code
n = 10

fun(n)
