# Implement pow(x, n), which calculates x raised to the power n (i.e., x^n).

"""Recursion Implementation """
def myPow_Recursive(x: float, n: int) -> float:
    def myPowHelper(acc, x, n):
        if n > 0:
            return myPowHelper(acc * x, x, n - 1)
        elif n < 0:
            return myPowHelper(acc / x, x, n + 1)
        else:
            return acc
    return myPowHelper(1, x, n)

# Leetcode didn't like recursion. THey fucked me with 2**31 as a power


""" Iterative Implementation """
def myPow_Iterative(x: float, n: int) -> float:
    acc = 1
    while n > 0:
        acc *= x
        n -= 1
    while n < 0:
        acc /= x
        n += 1
    return acc

# Apparently this approach is too naive. Says who! Okay, let's be smarter

def myPow_binExpo(x: float, n: int) -> float:
    acc = 1
    n1 = n
    while n1 > 0:
        if n1 % 2 == 0:
            x *= x
            n1 /= 2
        else:
            n1 -= 1
            acc *= x
    while n1 < 0:
        if n1 % 2 == 0:
            x *= x
            n1 /= 2
        else:
            n1 += 1
            acc /= x
    return acc

print(myPow_binExpo(0.00001, 2147483647))