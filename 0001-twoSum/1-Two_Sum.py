nums = [3,2,4]
target = 6
stop = False

for i in range(len(nums)):
    if stop:
        break
    for j in range(len(nums)):
        if (nums[i] + nums[j]) == target and i != j:
            print(i, j)
            stop = True
        if stop:
            break