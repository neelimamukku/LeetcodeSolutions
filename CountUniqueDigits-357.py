class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        f = 9
        s = 10
        if n == 0:
            return 1
        for i in range(2,n+1):
            f *= (10 - (i-1))
            s += f
        return s
