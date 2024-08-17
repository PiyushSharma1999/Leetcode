nums = [4, 2, 2, 3, 3, 3]

def findLen(nums):
    length = 0
    l = 0

    for r in range(len(nums)):
        if nums[l] != nums[r]:
            l = r
        length = max(length, r - l + 1)
    return length

print(findLen(nums))


            