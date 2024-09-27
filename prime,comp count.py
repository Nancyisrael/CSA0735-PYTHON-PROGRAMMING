list=[4,54,29,71,7,59,98,23]
pc=0
cc=0
for num in list:
  if num>1:
    is_prime=True
    for i in range(2,num):
      if num%i==0:
       cc+=1
       is_prime=False
       break
    if is_prime:
       pc+=1
print("composite count: ",cc)
print("prime count: ",pc)
