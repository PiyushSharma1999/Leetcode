nums = [3,2,4]
target = 6

def twoSum(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        l,r = 0, len(nums)-1
        while l<r:
            if nums[l] + nums[r] == target:
                return [l, r]
            elif nums[l] + nums[r] > target:
                r -= 1
            else:
                l += 1
        return []

print(twoSum(nums, target))

print(nums.index(3))