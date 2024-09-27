def longestSubstring(s, k):
    if len(s) < k:
        return 0
    for char in set(s):
        if s.count(char) < k:
            return max(longestSubstring(sub, k) for sub in s.split(char))
    return len(s)
s = "aaabb"
k = 3
print(longestSubstring(s, k))

def Substring(s):
    ans, temp = 1, 1
    for i in range(1, len(s)):
        if (s[i] == s[i - 1]):
            temp += 1
        else:
            ans = max(ans, temp)
            temp = 1
 
    ans = max(ans, temp)
    return ans

s = input("Enter the string: ")
print(Substring(s))
