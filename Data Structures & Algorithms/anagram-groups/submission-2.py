from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d1=defaultdict(list)
        for s in strs:
            count=[0]*26
            for j in s:
                count[ord(j)-ord('a')]=count[ord(j)-ord('a')]+1
            d1[tuple(count)].append(s)
        ls=[]
        for i,v in d1.items():
            ls.append(v)
        return ls
            
            