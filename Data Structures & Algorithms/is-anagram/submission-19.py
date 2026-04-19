from collections import defaultdict;
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s1=defaultdict(int)
        t1=defaultdict(int)
        for i in s:
            s1[i]=s1[i]+1
        for j in t:
            t1[j]=t1[j]+1
        if s1==t1:
            return True
        return False