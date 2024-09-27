bin1=input("enter the binary number1  :")
bin2=input("enter the binary number2 :")
bin3=input("enter the binary number3 :")
a=int(bin1,2)
b=int(bin2,2)
c=int(bin3,2)
if(a>b and a>c):
    print("Greatest : ",bin(a)[2:])
elif(b>a and b>c):
    print("Greatest : ",bin(b)[2:])
else:
     print("Greatest : ",bin(c)[2:])
    
