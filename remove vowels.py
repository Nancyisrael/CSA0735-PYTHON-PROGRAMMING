user_input = input("Enter a string: ")
vowels = "aeiouAEIOU"
no_vowels_string = ""
for char in user_input:
    if char not in vowels:
        no_vowels_string += char
print("The string without vowels is:", no_vowels_string)
