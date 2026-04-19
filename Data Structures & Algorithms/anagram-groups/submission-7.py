from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic=defaultdict(list)
        for s in strs:
            count=[0]*26
            for c in s:
                count[ord('a')-ord(c)]+=1
            dic[tuple(count)].append(s)
        res=[i for i in dic.values()]
        return res