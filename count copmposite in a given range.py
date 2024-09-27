A=12
B=19
for i in range(A,B+1):
    for j in range(2,i):
      if i%j==0:
        print(i)
        break
