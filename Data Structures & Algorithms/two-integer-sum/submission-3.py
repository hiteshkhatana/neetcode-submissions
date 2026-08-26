class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, v in enumerate(nums):
            second = target - v
            if second in nums and nums.index(second) != i:
                return sorted([i,nums.index(second)])