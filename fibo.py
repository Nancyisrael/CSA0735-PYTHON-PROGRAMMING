f=0
s=1
n=10
for i in range(1,n+1):
  print(f,end=" ")
  n=f+s
  f=s
  s=n
