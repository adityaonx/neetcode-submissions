class Solution:
    def trap(self, height: List[int]) -> int:
        total=0
        n=len(height)
        max_left=[0]
        max_right=[0]*n
        for i in range(1,n):
            max_left.append(max(max(max_left),height[i-1]))
        for j in range(n-2,-1,-1):
            max_right[j]=max(max(max_right),height[j+1])
        for i in range(n):
            vol=min(max_left[i],max_right[i])-height[i]
            if vol>0:
                total+=vol
        return total
        


                
