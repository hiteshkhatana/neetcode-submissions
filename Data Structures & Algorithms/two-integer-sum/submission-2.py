class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, v in enumerate(nums):
            second = target - v
            if second in nums:
                sindx = nums.index(second)
                if sindx != i:
                    return sorted([i,nums.index(second)])