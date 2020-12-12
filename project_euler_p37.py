# Truncatable Primes
from math import floor,sqrt

def is_truncatable(n):
    is_trunc = True
    temp = n
    length = 0
    # from right to left
    while temp > 0:
        if temp != 2:
            # number one will no go inside the for loop because then the range would be (2,2) i.e., i = 2, until i<2 which is not possible
            for i in range(2, floor(sqrt(temp))+1):
                if not temp%i:
                    return False
            if temp == 1:
                return False
        temp//=10
        length+=1
    # from left to right
    temp = n
    while length > 1:
        temp%=10**(length-1)
        for i in range(2, floor(sqrt(temp))+1):
            if temp != 2:
                if not temp%i:
                    return  False
        if temp == 1:
            return False
        length-=1

    return  True

# find prime numbers that has two digits or more
# loop for each left and right
num = 10  # gets incremented to pass to the checking function
count = 0  # when count equals 11 break out of the loop
sum_primes = 0  # sum all eleven truncatable primes
is_prime = True
while count < 11:
    for i in range(2,floor(sqrt(num))+1):
        if not num%i:
            is_prime = False
    if is_prime:
        if is_truncatable(num):
            print(num)
            count+=1
            sum_primes+=num
    num+=1
    is_prime = True

print(sum_primes)

