class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        d={}
        for i in s:
            d[i]=d.get(i,0)+1
        for j in t:
            if d.get(j): d[j]-=1
        for i,v in d.items():
            if v>0:
                return False
        return True