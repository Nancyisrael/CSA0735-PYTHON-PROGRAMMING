def count_bits(n):
   ans=[]
   for i in range(n+1):
        ans.append(bin(i).count('1'))
   return ans
n=2
print(count_bits(n))
