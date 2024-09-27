S1 = "sky is blue in color"
S2 = "Raj likes sky blue color"
words1 = S1.split()
words2 = S2.split()
result1 = [word for word in words1 if word not in words2]
result2 = [word for word in words2 if word not in words1]
print("S1:", ' '.join(result1))
print("S2:", ' '.join(result2))
