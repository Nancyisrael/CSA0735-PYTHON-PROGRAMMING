str="saveethaschoolofengineering"
vc=cc=0
for char in str:
    vowels="aeiouAEIOU"
    if char in vowels:
        vc+=1
    else:
        cc+=1
print("vowel count:",vc)
print("consonant count :",cc)

str="saveethaschoolofengineering"
vc=cc=0
for char in range(len(str)):
    if str[char]=='a' or str[char]=='e' or str[char]=='i' or str[char]=='o' or str[char]=='u':
        vc+=1
    else:
        cc+=1
print("vowel count:",vc)
print("consonant count :",cc)
