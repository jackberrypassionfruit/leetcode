height = [1,8,6,2,5,4,8,3,7]
# height = [1,1]

yesMax= 0
maybeMax = 0
i, j = 0, len(height) - 1
while i < j:
    a = height[i]
    b = height[j]
    maybeMax = min(a, b) * abs(i - j)
    if maybeMax > yesMax:
        yesMax = maybeMax
    if a > b:
        j -= 1
    else:
        i += 1
print(yesMax)
