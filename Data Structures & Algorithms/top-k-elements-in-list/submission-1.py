class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict1={}
        for i in nums:
            dict1[str(i)]=dict1.get(str(i),0)+1
        dicSort=sorted(dict1.items(),key=lambda item:(item[1],item[0]),reverse=True)
        ls=[]
        for i in range(k):
            ls.append(int(dicSort[i][0]))
        return ls

