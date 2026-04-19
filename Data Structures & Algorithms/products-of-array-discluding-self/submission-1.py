class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        res=[0]*n#[0,0,0,0]
        pref=[0]*n#[0,0,0,0]#[1,0,0,0]
        suff=[0]*n#[0,0,0,0]#[0,0,0,1]
        pref[0]=suff[n-1]=1
        for i in range(1,n):
            pref[i]=pref[i-1]*nums[i-1]#[1,1,4,8]
        for j in range(n-2,-1,-1):
            suff[j]=suff[j+1]*nums[j+1]#[48,24,6,1]
        for k in range(n):
            res[k]=pref[k]*suff[k]#[48,24,24,8]
        return res