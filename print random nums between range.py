import random
A = int(input("Enter A value: "))
B = int(input("Enter B value: "))
n = int(input("Enter number of elements: "))
random_list = []
for _ in range(n):
    random_number = random.randint(A, B)
    random_list.append(random_number)
print("Randomized list is:", random_list)
