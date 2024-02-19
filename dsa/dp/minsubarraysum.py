target = 7
nums = [2, 3, 1, 2, 4, 3]
l, r = 0, 0
min_sum = len(nums) + 1

while r <= len(nums):
    sublist = nums[l:r + 1]
    total = sum(sublist)

    if total == target:
        min_sum = min(min_sum, r - l + 1)
    elif total < target:
        r += 1
    else:
        l += 1
        r = l

print(min_sum)
