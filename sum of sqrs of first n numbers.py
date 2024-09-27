def sum_of_squares(n):
    sum = 0
    for i in range(1, n + 1):
        sum += i ** 2
    return sum

n = int(input("Enter a positive integer: "))
print("Sum of squares of first", n, "natural numbers is:", sum_of_squares(n))
