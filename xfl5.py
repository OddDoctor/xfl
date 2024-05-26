def gcd(a, b):
    """Compute the Greatest Common Divisor (GCD) of two numbers using the Euclidean algorithm."""
    while b != 0:
        a, b = b, a % b
    return a

# Example usage
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

result = gcd(num1, num2)
print(f"The GCD of {num1} and {num2} is {result}")
