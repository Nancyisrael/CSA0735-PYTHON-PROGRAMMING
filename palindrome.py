n=121
k=n
rev=0
while n>0:
    rev=rev*10+n%10
    n//=10
if rev==k:
   print("palindrome")
else:
   print("not a palindrome")
