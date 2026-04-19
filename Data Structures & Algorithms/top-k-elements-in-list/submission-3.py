class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d1={}
        for n in nums:
            d1[n]=d1.get(n,0)+1
        ls_of_ls=[[] for _ in range(len(nums)+1)]
        
        for num,freq in d1.items():
            ls_of_ls[freq].append(num)
        
        res=[]
        for i in range(len(nums),0,-1):
            for n in ls_of_ls[i]:
                res.append(n)
                if len(res)==k:
                    return res


            
        

        