class Solution:
    def trap(self, height: List[int]) -> int:
        max_left=0
        max_right=0
        n=len(height)
        total=0
        left=0
        right=n-1
        while left<right:
            if height[left]<=height[right]:
                max_left=max(max_left,height[left])
                area=max_left-height[left]
                left+=1
            else:
                max_right=max(max_right,height[right])
                area=max_right-height[right]
                right-=1
            if area>0:total+=area
        return total    

                
