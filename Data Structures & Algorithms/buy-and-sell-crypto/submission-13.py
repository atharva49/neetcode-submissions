class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprofit = 0
        l=0
        r=1

        while r < len(prices):
            if prices[r] <= prices[l]:
                l=r
            profit = prices[r] - prices[l]
            maxprofit = max(maxprofit,profit)
            r+=1
            print(profit)

        return maxprofit