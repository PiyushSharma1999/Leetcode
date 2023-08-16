# O(n)
def maximum_subarray(input_array):
    maxSub = input_array[0]
    current_sum = 0

    for n in input_array:
        if current_sum < 0:
            current_sum = 0
        current_sum += n
        maxSub = max(maxSub, current_sum)
    return maxSub


s = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(maximum_subarray(s))