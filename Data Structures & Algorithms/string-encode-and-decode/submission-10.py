class Solution:

    def encode(self, strs: List[str]) -> str:
        encstr=""
        for s in strs:
            encstr=encstr+str(len(s))+"#"+s
        return encstr
    def decode(self, s: str) -> List[str]:
        # 11#StringChuck5#Flick
        i=0
        ls=[]
        while i<len(s):
            j=i
            while s[j]!="#":
                j+=1
            lenn=int(s[i:j])
            i=j+1
            j=i+lenn
            ls.append(s[i:j])
            i=j
        return ls

        
            