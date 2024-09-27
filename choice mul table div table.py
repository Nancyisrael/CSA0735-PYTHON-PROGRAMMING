number = int(input ("Enter the number of which the user wants to print the multiplication table: "))
n= int(input ("Enter till which number table should be printed: "))
choice=int(input ("Enter the choice "))
print ("The Multiplication Table of: ", number)    

if(choice==1):
   for count in range(1, n+1):      
      print(number, 'x', count, '=', number * count)
elif(choice==2):
   for c in range(1, n+1):
      y=number * c
      print(y, '/', number, '=',c)
else:
    print("invalid")
