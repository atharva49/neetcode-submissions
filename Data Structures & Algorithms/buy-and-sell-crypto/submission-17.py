class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l=0
        profit = 0
        r=1

        while r<=len(prices)-1:
            if prices[l]>=prices[r]:
                l=r
            profit = max(profit,prices[r]-prices[l])
            r+=1
            
        return profit