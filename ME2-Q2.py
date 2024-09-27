N=8
f=0
s=1
y=[]
for i in range(N):
    y.append(f)
    n=f+s
    f=s
    s=n
print(y)
print(N,"th fibonacci number is :",y[N-1])
