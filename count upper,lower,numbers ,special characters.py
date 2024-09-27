uc=lc=d=sp=0
while True:
    ch=input("enter any character :")
    if ch=="*":
        break
    if ch.isalpha():
        if ch.isupper():
            uc+=1
        elif ch.islower():
            lc+=1
    elif ch.isdigit():
        d+=1
    else:
        sp+=1
print("upper count :",uc)
print("lower count :",lc)
print("digits count :",d)
print("sp count :",sp)
