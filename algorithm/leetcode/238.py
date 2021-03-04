class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length=len(nums)
        dp1,dp2=[0]*length,[0]*length
        
        dp1[0]=1
        dp2[length-1]=1
        for i in range(1,length):
            dp1[i]=nums[i-1]*dp1[i-1]
        for j in range(length-2,-1,-1):
            dp2[j]=nums[j+1]*dp2[j+1]
        return [dp1[k]*dp2[k] for k in range(length)]
        