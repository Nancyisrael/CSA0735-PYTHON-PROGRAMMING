word = input("Enter the word: ")
repeated_letters = []
for letter in word:
    if word.count(letter) > 1 and letter not in repeated_letters:
        repeated_letters.append(letter)
print("Number of repeated letters =", len(repeated_letters))
if repeated_letters:
    print("Repeated letter(s) =", " ".join(repeated_letters))
