class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, v in enumerate(nums):
            second = target - v
            if second in seen:
                return [seen[second],i]
            seen[v] = i