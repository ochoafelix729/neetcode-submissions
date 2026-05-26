from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        table = defaultdict(list)
        for word in strs:
            counts = [0] * 26
            for c in word:
                counts[ord(c) - ord('a')] += 1

            table[tuple(counts)].append(word)

        return list(table.values())