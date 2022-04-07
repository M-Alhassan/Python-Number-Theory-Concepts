#Q1 (install IDE): Done

#Q2 (Print my_Primes[]):
#note: I used Sieve of Eratosthenes's algorithm to make it as efficient as possible
def Q2():
    my_Primes = []
    num = 20
    numbers = set(range(num, 1, -1))
    while numbers:
        p = numbers.pop()
        my_Primes.append(p)
        numbers.difference_update(set(range(p*2, num+1, p)))

    for i in range(len(my_Primes)):
        print(my_Primes[i])

#Q3 (Eucleadian's Algorithm to find GCD):
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)

#Q4 (FLT to check primality):
#note: power is a helper function
import random
 
def is_prime(n, k):  
    if n == 1 or n == 4:
        return False
    elif n == 2 or n == 3:
        return True
    else:
        for i in range(k):
            a = random.randint(2, n - 2)
            if power(a, n - 1, n) != 1:
                return False
                 
    return True
             
def power(a, n, p):
    result = 1
    a = a % p 
    while n > 0:
        if n % 2:
            result = (result * a) % p
            n = n - 1
        else:
            a = (a ** 2) % p
            n = n // 2
             
    return result % p
     
#main:
print('----- Q1 -----')
print('IDE is installed')
print('----- Q2 -----')
print('listing all prime numbers less than 20:')
Q2()
print('----- Q3 -----')
print('The GCD of 123 and 456 is:')
print(gcd(123, 456))
print('----- Q4 -----')
print('is 324^234 a prime number?')
if is_prime((24**234), 3):
    print('is prime')
else:
    print('not prime')

print('----- Q5 -----')
k = 3
prime_list = []
for i in range(2, 2000):
    if is_prime(i, k):
        prime_list.append(i)
for i in range(len(prime_list)):
    print(prime_list[i])