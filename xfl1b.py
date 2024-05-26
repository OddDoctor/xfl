def is_prime(n):
    if(n <= 1):
        return False
    if(n <= 2):
        return True
    if(n % 2 == 0):
        return False
    for i in range(3, int(n/2)):
        if n % i == 0:
            return False
    return True

number = 27
print(f'Is {number} a prime number: {is_prime(number)}')