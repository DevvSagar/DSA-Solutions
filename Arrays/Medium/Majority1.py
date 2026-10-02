nums = [7, 0, 0, 1, 7, 7, 2, 7, 7]


def majorityElement(nums):
        frequency = {}
        for item in nums:
            if item in frequency:
                frequency[item] += 1 
            else:
                frequency[item] = 1
        print(frequency)
        max_freq = 0
        ans = 0
        for key , value in frequency.items():
            if value > max_freq:
                max_freq = value
                ans = key
        return ans

print(majorityElement(nums))

