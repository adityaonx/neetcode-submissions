class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #min-heap
        count={}
        for n in nums:
            count[n]=count.get(n,0)+1
        heap=[]
        for num in count:
            heapq.heappush(heap,(count[num],num))
            if k<len(heap):
                heapq.heappop(heap)
        res=[]
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res

        


            
        

        