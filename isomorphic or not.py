def is_isomorphic(s, t):
    if len(s) != len(t):
        return False
    mapping = {}
    for i in range(len(s)):
        if s[i] in mapping:
            if mapping[s[i]] != t[i]:
                return False
        else:
            if t[i] in mapping.values():
                return False
            mapping[s[i]] = t[i]
    return True
s = "egg"
t = "add"
print(is_isomorphic(s, t))
