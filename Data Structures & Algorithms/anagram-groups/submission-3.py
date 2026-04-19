class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        lss={}
        for s in strs:
            zeros=[0]*26 
            for i in s:
                zeros[ord('a')-ord(i)]+=1
            lss[tuple(zeros)]=lss.get(tuple(zeros),[])
            lss[tuple(zeros)].append(s)
        ls=[]
        for k,v in lss.items():
            ls.append(v)
        return ls
        
