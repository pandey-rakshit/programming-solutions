class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        prodN = 1
        sumN = 0
        while n > 0:
            rem = n % 10
            prodN *= rem
            sumN += rem
            n = n // 10
        return prodN - sumN
