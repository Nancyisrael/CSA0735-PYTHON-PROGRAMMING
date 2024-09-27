n=5
for i in range(1,n+1):
    if i%3==0 and i%5==0:
        print("fizzBuzz",end=",")
    elif i%3==0:
        print("Fizz",end=",")
    elif i%5==0:
        print("buzz",end=",")
    else:
        print(i,end=",")
