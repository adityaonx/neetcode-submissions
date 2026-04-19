from collections import defaultdict 
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d=defaultdict(list)
        for item in strs:
            count=[0]*26
            for char in item:
                count[ord(char)-ord('a')]=count[ord(char)-ord('a')]+1
            d[tuple(count)].append(item)
        ls=[]
        for i,v in d.items():
            ls.append(v)
        return ls
                

            