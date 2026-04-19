class Solution:

    def encode(self, strs: List[str]) -> str:
        enc=""
        for i in strs:
            enc=enc+"#e1d1888#"+i
        return enc
    def decode(self, s: str) -> List[str]:
        if len(s)==0:
            return []
        items=s.split("#e1d1888#")[1:]
        ls=[]
        for i in items:
            ls.append(i)
        return ls
