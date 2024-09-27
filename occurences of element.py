numbers = (3, 6, 8, 9, 8, 9, 12, 35, 8)
target = 8
count = 0
for num in numbers:
    if num == target:
        count += 1
print("The target number", target, "occurs", count, "times.")

