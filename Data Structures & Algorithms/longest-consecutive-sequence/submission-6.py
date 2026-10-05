class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_streak = 0
        nums = set(nums)
        for num in nums:
            if num - 1 in nums:
                continue
            next_num = num + 1
            streak = 1
            while next_num in nums:
                next_num += 1
                streak += 1
            max_streak = max(max_streak,streak)
        return max_streak
