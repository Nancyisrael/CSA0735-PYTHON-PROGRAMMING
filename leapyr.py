d=int(input("enter date:"))
m=int(input("enter month:"))
y=int(input("enter year :"))
if(y%4==0 or y%400==0) and (y%100!=0):
    print("leap year:")
else:
        print("not a leap year:")
        
