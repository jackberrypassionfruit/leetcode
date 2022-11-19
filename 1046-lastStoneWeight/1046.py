stones = [2,7,4,1,8,1]

while len(stones) > 1:
    h1 = 0
    h2 = 0
    print(stones)

    for i in range(len(stones)):
        if stones[i] > stones[h1]:
            h2 = h1
            h1 = i
        elif stones[i] == stones[h1]:
            h2 = h1
        elif stones[i] < stones[h1] and stones[i] > stones[h2]:
            h2 = i
        print("h1 is", h1, "and h2 is: ", h2)
        
    if stones[h1] == stones[h2]:
        stones.pop(h1)
        stones.pop(h2)
    else:
        stones[h1] = stones[h1] - stones[h2]
        stones.pop(h2)

if not stones:
    print(0)
print(stones[0])