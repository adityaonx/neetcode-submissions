class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res=set(nums)
        nums.sort()
        out=set()
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                for k in range(j+1,len(nums)):
                    if nums[i]+nums[j]+nums[k]==0:
                        tmp=[nums[i],nums[j],nums[k]]
                        out.add(tuple(tmp))
        ls=[list(i) for i in out]
        return ls