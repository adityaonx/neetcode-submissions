class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count={}
        for n in nums:
            count[n]=count.get(n,0)+1
        ls=[]
        for num,cnt in count.items():
            ls.append([cnt,num])
        ls.sort()
        res=[]
        while len(res)<k:
            res.append(ls.pop()[1])
        return res


        


            
        

        