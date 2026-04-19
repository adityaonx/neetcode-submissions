class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res={}
        for i,num in enumerate(nums):
            rem=target-num
            if rem in res:
                return [res[rem],i]
            else:
                res[num]=i
            
        