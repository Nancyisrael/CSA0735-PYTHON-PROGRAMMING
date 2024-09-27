str="Modi Birthday @September 17,#&$%"
v=""
c=""
d=""
s=""
vowels="aeiouAEIOU"
vc=cc=dc=sp=sc=0
for char in str:
    if char.isalpha():
        if char in vowels:
            v+=char
            vc+=1
        else:
            c+=char
            cc+=1
    elif char.isdigit():
        d+=char
        dc+=1
    elif char==" ":
        sp+=1
    else:
        s+=char
        sc+=1
print("vowels :",v)
print("vowels count :",vc)
print("consonants :",c)
print("consonants count :",cc)
print("digits :",d)
print("digits count :",dc)
print("spaces count :",sp)
print("special characters :",s)
print("special characters count :",sc)
        
            
    
