mport itertools

num = input("Enter a number: ")
perms = itertools.permutations(num)

print("Permutations are:")
for perm in perms:
    print("".join(perm))


