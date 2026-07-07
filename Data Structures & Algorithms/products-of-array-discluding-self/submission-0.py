class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        a=[1]*n
        p=1
        for i in range(n):
            a[i]=p
            p*=nums[i]
        s=1
        for i in range(n-1,-1,-1):
            a[i]*=s
            s*=nums[i]
        return a