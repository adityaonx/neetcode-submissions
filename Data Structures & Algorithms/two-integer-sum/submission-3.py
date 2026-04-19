class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d={}
        for i,num in enumerate(nums):
            rem=target-num
            if rem in d:
                return [d[rem],i]
            else:
                d[num]=i 