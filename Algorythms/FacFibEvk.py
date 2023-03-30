#sum of all numbers in(like 5 = 1+2+3+4+5 = 15)
def sum(x):
    if x == 0:
        return 0
    elif x == 1:
        return 1
    else:
        return x + sum(x-1)
z = sum(5)
print(z)

#Factorial
def factorial(x):
    if x == 0:
        return 1
    else:
        return x * factorial(x-1)
print(factorial(5))

#Fibonacci
def fibo(x):
     if x == 0:
         return 0
     elif x == 1:
         return 1
     else:
         return fibo(x-1) + fibo(x-2)
print(fibo(60))

#Evklid
def gcd(a, b):
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    return a + b
gcd(500,600)