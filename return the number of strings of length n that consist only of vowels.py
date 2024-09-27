n = 2
count = 0
vowels = 'aeiou'
for i in range(5**n):
    string = ''
    for j in range(n):
        string += vowels[i // (5**j) % 5]
    if string == ''.join(sorted(string)):
        count += 1
print(count)
