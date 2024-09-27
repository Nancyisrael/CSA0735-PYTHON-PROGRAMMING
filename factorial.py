fact=1
n=-5
if n<0:
    print("factorial not defined")
elif n==0 or n==1:
    print("factorial :",fact)
else:
    for i in range(1,n+1):
        fact=fact*i
    print("factorial of ",n," is ",fact)
