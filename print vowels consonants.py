str="engineering"
v=[]
c=[]
for i in range(len(str)):
    if str[i]=='a' or str[i]=='e' or str[i]=='i' or str[i]=='o' or str[i]=='u':
        v.append(str[i])
    else:
        c.append(str[i])
print("vowels :",v)
print("consonants :",c)
