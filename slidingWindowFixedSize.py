nums = [1,2,4,3,3]
k = 2

def closeDuplicates(nums, k):
    window = set()
    l = 0

    for r in range(len(nums)):
        if r - l + 1 > k:
            window.remove(nums[l])
            l += 1
        if nums[r] in window:
            return True
        window.add(nums[r])
    
    return False

print(closeDuplicates(nums, k))