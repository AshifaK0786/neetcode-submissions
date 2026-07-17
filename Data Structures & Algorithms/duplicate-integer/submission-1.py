class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        return (any(nums.count(num) > 1 for num in nums))
        