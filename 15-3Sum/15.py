"""
Find all of the triplets between the 3 numbers that add up to 0
"""

nums = [-1,0,1,2,-1,-4,-2,-3,3,0,4]
trips = []
length = range(len(nums))
breakout = False

# for i in length:
#     for j in length:
#         for k in length:
#             a = nums[i]
#             b = nums[j]
#             c = nums[k]
#             if a + b + c == 0 and i != j and j != k and i != k:
#                 breakout = False
#                 for trip in trips:
#                     if a in trip and b in trip and c in trip:
#                         breakout = True
#                 if breakout:
#                     continue
#                 trips.append([a, b, c])



nums.sort()
print(nums)
ans = []

for i in range(len(nums)):
    l = i + 1
    r = len(nums) - 1
    a = nums[i]
    if i > 0 and nums[i] == nums[i -1]:
        continue
    while l < r:
        threeSum = a + nums[l] + nums[r]
        if threeSum < 0:
            l += 1
            # print(threeSum)
        elif threeSum > 0:
            r -= 1
        else:
            ans.append([a, nums[l] ,nums[r]])
            l += 1
            while nums[l] == nums[l -1] and l < r:
                l += 1


print(ans)