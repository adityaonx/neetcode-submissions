class Solution:
    def maxArea(self, heights: List[int]) -> int:
        total=0
        start=0
        end=len(heights)-1
        while start<end:
            width=abs(end-start)
            area=min(heights[start],heights[end])*width
            total=max(total,area)
            if heights[start]<heights[end]:
                start+=1
            else:
                end-=1
        return total
            
            

            
