def is_tech_number(n):
    return '3' in str(n) and '7' in str(n)

num = int(input("Enter a number: "))
if is_tech_number(num):
    print(num, "is a tech number")
else:
    print(num, "is not a tech number")

