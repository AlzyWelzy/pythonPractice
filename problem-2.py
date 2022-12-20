def factorial(x):
    if x == 1:
        return 1
    else:
        return x * factorial(x - 1)


num = int(input("Enter a positive integer: "))

if num < 0:
    print("Sorry, Factorial doesn't exist for negative numbers.")
elif num == 0 or num == 1:
    print(f"The Factorial of {num} is 1.")
else:
    result = factorial(num)
    print(f"The Factorial of {num} is {result}.")
