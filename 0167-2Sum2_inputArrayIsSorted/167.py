nums = [2,7,11,15]

target = 9

def twoSumNestedLoops(numbers, target):
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if numbers[i] + numbers[j] == target and i != j:
                return list([i + 1, j + 1])

def twoSumPointers(numbers, target):
    i = 0
    j = len(numbers) - 1
    while i < j:
        if numbers[i] + numbers[j] > target:
            j -= 1
        elif numbers[i] + numbers[j] < target:
            i += 1
        else:
            return list([i + 1, j + 1])
        



print(twoSumPointers(nums, target))