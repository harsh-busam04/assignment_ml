1) n = int(input("Enter a positive integer: "))
if n > 0:
    for i in range(1, n + 1):
        print(i)
    total = 0
    counter = 1
    while counter <= n:
        total += counter
        counter += 1
    print("Sum of numbers from 1 to", n, "is:", total)
else:
    print("Please enter a positive integer.")


2) def calculate_square(n):
    return n ** 2

try:
    num = int(input("Enter a positive integer: "))
    if num > 0:
        print(f"The square of {num} is {calculate_square(num)}.")
    else:
        print("Please enter a positive integer.")
except ValueError:
    print("Invalid input! Please enter an integer.")
