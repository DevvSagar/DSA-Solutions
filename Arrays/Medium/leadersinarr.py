nums = [1, 2, 5, 3, 1, 2]

def leaders(nums):
    lead = [nums[-1]]
    i = len(nums) - 2
    curr_leader = nums[-1]
    while i >= 0:
        if nums[i] > curr_leader:
            lead.append(nums[i])
            curr_leader = nums[i]
        i-=1
    lead.reverse()
    return lead

print(leaders(nums))