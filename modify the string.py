S = "ghee"
result = ""
for char in S:
    count = S.count(char)
    new_char = chr((ord(char) - 97 + count) % 26 + 97)
    result += new_char
print(result)
