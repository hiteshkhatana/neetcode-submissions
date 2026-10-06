from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        outputs = defaultdict(list)
        for word in strs:
            lwords = "".join(sorted(list(word)))
            outputs[lwords].append(word)
        return list(outputs.values())