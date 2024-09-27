S1 = 'welcome'
S2 = 'Homely'
S3 = ''
len1 = len(S1)
len2 = len(S2)
max_len = max(len1, len2)
for i in range(max_len):
    if i < len1:
        S3 += S1[i]
    if i < len2:
        S3 += S2[i]
vowels = 'aeiouAEIOU'
vowel_count = 0
for char in S3:
    if char in vowels:
        vowel_count += 1
print("Combined String (S3) =", S3)
print("Number of vowels in S3 =", vowel_count)
