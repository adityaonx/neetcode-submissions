class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        dict={}
        for i in s:
            dict[i]=dict.get(i,0)+1
        for j in t:
            if j not in dict.keys() or dict[j]==0:
                return False
            dict[j]-=1
        return True
        