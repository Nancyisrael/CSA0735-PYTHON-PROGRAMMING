def removeElement(nums, val):
    k = 0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[k] = nums[i]
            k += 1
    
    return k
nums1 = [3, 2, 2, 3]
val1 = 3
k1 = removeElement(nums1, val1)
print(k1, nums1[:k1])
