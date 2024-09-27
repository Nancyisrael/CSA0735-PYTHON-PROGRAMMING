S1="What"
S2="Watch"
count=0
len=min(len(S1),len(S2))
for i in range(len):
    if S1[i].lower()==S2[i].lower():
        count+=1
print("number of matches:",count)
