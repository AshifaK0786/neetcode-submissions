class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        c={}
        for n in nums:
            c[n]=c.get(n,0)+1
            if c[n]>len(nums)//2:
                return n