from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sortedd=defaultdict(list)
        for s in strs:
            sortedd[tuple(sorted(s))].append(s)
        ls=[]
        for i,v in sortedd.items():
            ls.append(v)
        return ls
    
        
