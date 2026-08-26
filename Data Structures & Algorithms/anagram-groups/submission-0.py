class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        outputs = {}
        for word in strs:
            lwords = "".join(sorted(list(word)))
            if lwords in outputs:
                outputs[lwords].append(word)
            else:
                outputs[lwords] = [word]
        return list(outputs.values())