def missing(nums):
    n=len(nums)
    expect_sum=n*(n+1)//2
    actual_sum=sum(nums)
    return expect_sum-actual_sum
nums=[3,0,1]
print("missing number: ",missing(nums))
