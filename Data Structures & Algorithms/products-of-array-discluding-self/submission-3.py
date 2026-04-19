class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ls=[]
        for i in range(len(nums)):
            prod=1
            for j in range(len(nums)):
                if i!=j:
                    print(i,"i and j",j)
                    prod=prod*nums[j]
            ls.append(prod)
        return ls
