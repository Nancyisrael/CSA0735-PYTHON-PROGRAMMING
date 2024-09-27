nums=[4,54,29,71,7,59,98,23]
pc=cc=0
for i in range(len(nums)):
    for j in range(2,nums[i]):
        if(nums[i]%j==0):
            cc+=1
            break
    else:
            pc+=1
print("prime count :",pc)
print("composite count :",cc)
