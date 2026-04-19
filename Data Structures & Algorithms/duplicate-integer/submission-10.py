class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen={}
        for i in nums:
            if seen.get(i):
                return True
            else:
                seen[i]=True
        return False