class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ls=[]
        for i in range(len(nums)):
            pr=1
            for j in range(len(nums)):
                if j!=i:
                    pr*=nums[j]
            ls.append(pr)
        return ls