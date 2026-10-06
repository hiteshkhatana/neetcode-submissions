from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        Counts = Counter(nums)
        ans = sorted(Counts, key=lambda x:Counts[x], reverse=True)
        return ans[:k]