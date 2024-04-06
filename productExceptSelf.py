nums = [1, 2, 3, 4]

def productExceptSelfdiv(nums):
    res = []
    temp = nums.copy()
    for i in range(len(temp) - 1):
        product = temp[i] * temp[i+1]
        temp[i+1] = product
    
    for i in nums:
        res.append(product//i)
    return res

def productExceptSelf(nums):
    res = [1] * len(nums)

    prefix = 1
    for i in range(len(nums)):
        res[i] = prefix
        prefix *= nums[i]
    
    postfix = 1
    for i in range(len(nums)-1, -1, -1):
        res[i] *= postfix
        postfix *= nums[i]

    return res



print(productExceptSelf(nums))


#[24, 12, 8, 6]



