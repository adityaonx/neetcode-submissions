class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        seen={}
        for i,num in enumerate(numbers,start=1):
            if target-num in seen:
                return[seen[target-num],i]
            seen[num]=i

            


