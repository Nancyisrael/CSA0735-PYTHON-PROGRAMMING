n=14567
k=n
rev=0
while n>0:
   rev=rev*10+n%10
   n//=10
print("reverse number: ",rev)
if(rev==k):
  print("palindrome")
else:
    print("not a plaindrome")
