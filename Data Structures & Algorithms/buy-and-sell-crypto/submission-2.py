class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l=0
        r=1
        max_p=0
        while r<len(prices):
            if prices[l]<prices[r]:
                prof=prices[r]-prices[l]
                max_p=max(prof,max_p)
            else:
                l=r
            r+=1
        return max_p