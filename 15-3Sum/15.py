"""
Find all of the triplets between the 3 numbers that add up to 0
"""

nums = [-1,0,1,2,-1,-4]
trips = []
length = range(len(nums))
print(length)
z = 0

for i in length:
    for j in length:
        for k in length:
            a = nums[i]
            b = nums[j]
            c = nums[k]
            if a + b + c == 0 and i != j and j != k and i != k:
                # for trip in trips:
                #     trips.append([a, b, c])
                # It hated this. I was trying to append into a list that it was already iterating over for the for loop. Basically just nullified anything I was doing in there. NO error though!


            print(z)

print(trips)