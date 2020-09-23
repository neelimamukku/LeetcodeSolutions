class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if prices == []:
            return 0
        minele = prices[0]
        maxDiff = 0
        for i in prices[1:]:
            if maxDiff < (i-minele):
                maxDiff = i-minele
            if minele > i:
                minele = i
        return maxDiff
