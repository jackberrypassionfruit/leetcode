nums = [-1,-100,3,99]

# Naive way, too much memory usage
# def rotate(list, k):
#     l = list[:-1*k]
#     r = list[-1*k:]
#     list = r + l

#     print(list)


# Clever way with math
# Not fast enough apparently
# k makes it iteration len(nums) times
# probably should make it swap with an index k over instead
def rotate(nums, k):
    for j in range(k):
        last_change = nums[1] - nums[0]
        current_change = last_change
        
        for i in range(2, len(nums)):
            current_change = nums[i] - nums[i - 1]
            nums[i - 1] -= last_change
            last_change = current_change

        current_change = nums[0] - nums[-1]
        nums[-1] -= last_change
        last_change = current_change

        nums[0] -= last_change

    print(nums)


rotate(nums, 2)