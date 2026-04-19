class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d1={}
        for i,n in enumerate(nums):
            rem=target-n
            if rem in d1.keys():
                return [d1[rem],i]
            d1[n]=i