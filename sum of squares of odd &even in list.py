n=int(input("enter number of elements:"))
I=[]
for i in range(n):
    I.append(int(input("enter the elements: ")))
def sum_squares(I):
   odd=sum(i**2 for i  in I if i%2!=0)
   even=sum(i**2 for i  in I if i%2==0)
   return [odd,even]
print("sum of squares of odd and even :",sum_squares(I))
