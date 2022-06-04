numbers = [1,0,1]

# Using a Bubble-Up approach
# Not pointer/math based

def moveZerosBubble(nums):
    not_done = True
    while not_done:
        not_done = False
        for i in range(1, len(nums)):
            if nums[i - 1] == 0 and nums[i - 1] != nums[i]:
                not_done = True
                nums[i - 1], nums[i] = nums[i], nums[i - 1]
                print(nums)


def moveZerosExtraSpace(nums):
    ans = []
    zeros = []
    for i in range(len(nums)):
        if not nums[i] == 0:
            ans.append(nums[i])
        else:
            zeros.append(0)
    ans += zeros
    
    return ans

def moveZeros(nums):
    j = 0
    for i in range(1, len(nums)):
        if nums[i] != 0 and nums[j] == 0:
            nums[i], nums[j] = nums[j], nums[i]
            j += 1
        elif nums[j] != 0:
            j += 1

moveZeros(numbers)
print(numbers)