from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ls=defaultdict(list)
        for s in strs:
            count=[0]*26
            for c in s:
                count[ord('a')-ord(c)]+=1
            ls[tuple(count)].append(s)
        ret=[]
        for i,v in ls.items():
            ret.append(v)
        return ret
        
