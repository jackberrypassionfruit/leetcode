# Not Final Solution

def firstBadVersion(n: int) -> int:
        l = 0
        r = n - 1
        while r - l > 1:
            mid = (l + r) // 2

                
            if mid > 1:
                r = mid
            else:
                l = mid
        return r


print(firstBadVersion(5))