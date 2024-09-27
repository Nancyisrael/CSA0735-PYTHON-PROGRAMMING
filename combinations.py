def find_combinations(num):
   digits=[int(d) for d in str(num)]
   for i in range(3):
     for j in range(3):
       for k in range(3):
           
              if i!=j and j!=k and k!=i :
                 print(digits[i],digits[j],digits[k])
num=int(input("enter the number: "))
find_combinations(num)
