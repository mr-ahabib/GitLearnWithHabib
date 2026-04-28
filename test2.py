def two_sum(nums, target):
    mp = {}
    for i, x in enumerate(nums):
        if target - x in mp:
            return [mp[target - x], i]
        mp[x] = i
print(two_sum([2, 7, 11, 15], 9))