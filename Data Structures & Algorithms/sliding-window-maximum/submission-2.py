class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        arr=[]
        n=len(nums)
        for i in range(n-k+1):
            win=nums[i:i+k]
            arr.append(max(win))
        return (arr)

        