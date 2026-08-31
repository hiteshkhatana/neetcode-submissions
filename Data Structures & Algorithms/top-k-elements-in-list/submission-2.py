class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hmap = {}
        for elem in nums:
            if elem in hmap:
                hmap[elem] += 1  
            else:
                hmap[elem] = 1
        return sorted(hmap, key=hmap.get, reverse=True)[:k]