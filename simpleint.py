def interest(princi541pal,time,sc,g):
    if(sc=='y' and g=='m'):
        rate=12
    elif(sc=='y' and g=='f'):
        rate=15
    else:
        rate=10
    return (principal*time*rate)/100
principal=int(input("enter the amount : "))
time=int(input("enter the year : "))
sc=input("enter senior citizen or not(y/n) : ")
g=input("enter male or female(m/f) : ")
print("simple interest : ",interest(principal,time,sc,g))
      
