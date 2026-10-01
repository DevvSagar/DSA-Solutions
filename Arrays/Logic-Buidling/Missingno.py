nums = [3,0,1]

def missing_num(nums):
    n = len(nums)
    expected_sum = n * (n+1) // 2
    actual_sum = 0
    for i in nums:
        actual_sum += i
    return expected_sum - actual_sum

print(missing_num(nums))