class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        l=0
        r=n-1
        max_profit=0
        for i in range(n):
            for j in range(i,n):
                if prices[j]>prices[i]:
                    profit=prices[j]-prices[i]
                    max_profit=max(profit,max_profit)
        return max_profit