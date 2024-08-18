nums = [2, 7, 11, 15]
target = 9

def twoSum(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        prev = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in prev:
                return [prev[diff], i]
            else:
                prev[n] = i
        return []

print(twoSum(nums, target))

