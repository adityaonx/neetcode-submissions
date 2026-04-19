class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen_dict={}#{1:1,2:2,3:3}
        for num in nums:
            seen_dict[num]=seen_dict.get(num,0)+1
        ls=[[] for _ in range(len(nums)+1)]#[[],[1],[2],[3],[],[],[]]
        for i,v in seen_dict.items():
            ls[v].append(i)
        out_ls=[]
        for i in range(len(ls)-1,0,-1):
            for num in ls[i]:
                out_ls.append(num)
                if len(out_ls)==k:
                    return out_ls