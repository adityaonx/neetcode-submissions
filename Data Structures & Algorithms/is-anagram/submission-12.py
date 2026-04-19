class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)==len(t):
            s1=list(s)
            s2=list(t)
            for _ in range(len(s1)):
                if len(s1)>0 and s1[-1] in s2:
                    s2.remove(s1.pop())
            if len(s2)==0:
                return True
        return False
