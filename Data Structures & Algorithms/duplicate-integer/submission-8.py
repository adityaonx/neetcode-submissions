class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dup=[]
        for i in nums:
            if i not in dup:
                dup.append(i)
            elif i in dup:
                return True
        return False