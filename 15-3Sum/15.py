"""
Find all of the triplets between the 3 numbers that add up to 0
"""

nums = [-4,-2,1,-5,-4,-4,4,-2,0,4,0,-2,3,1,-5,0]
trips = []
length = range(len(nums))
breakout = False

for i in length:
    for j in length:
        for k in length:
            a = nums[i]
            b = nums[j]
            c = nums[k]
            if a + b + c == 0 and i != j and j != k and i != k:
                breakout = False
                for trip in trips:
                    if a in trip and b in trip and c in trip:
                        breakout = True
                if breakout:
                    continue
                trips.append([a, b, c])

print(trips)