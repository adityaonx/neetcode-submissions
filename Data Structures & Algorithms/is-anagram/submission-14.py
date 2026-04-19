class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        s1={}
        for i in s:
            s1[i]=s1.get(i,0)+1
        for i in t:
            if i not in s1 or s1[i]==0:
                return False
            s1[i]-=1
        return True