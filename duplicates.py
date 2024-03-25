nums = [3,1,1]
def dups(nums):
    nums = sorted(nums)
    for index in range(0, len(nums)-1):
        if nums[index] == nums[index+1]:
            return True
    return False

def dups_hset(nums):
    hashSet = set()
    for i in nums:
        if i in hashSet:
            return True
        else:
            hashSet.add(i)
    return False





print(dups(nums)) 
    