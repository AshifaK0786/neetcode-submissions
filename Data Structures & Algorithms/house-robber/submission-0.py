class Solution:
    def rob(self, nums: List[int]) -> int:
        e=0
        o=0
        for i in range(len(nums)):
            if i%2==0:
                e+=nums[i]
            else:
                o+=nums[i]
        if e<=o:
            return o
        else:
            return e
        