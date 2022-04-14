# Implement pow(x, n), which calculates x raised to the power n (i.e., x^n).
def myPow(x: float, n: int) -> float:
    def myPowHelper(acc, x, n):
        if n > 0:
            return myPowHelper(acc * x, x, n - 1)
        elif n < 0:
            return myPowHelper(acc / x, x, n + 1)
        else:
            return acc
    return myPowHelper(1, x, n)

print(myPow(2, -1))