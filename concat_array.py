def getConcatenation(nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        capacity = 2 * len(nums)
        new_arr = [0] * capacity
        for i in range(len(nums)):
            new_arr[i], new_arr[i+len(nums)] = nums[i], nums[i]
        return new_arr

print(getConcatenation([1,2,3]))
            