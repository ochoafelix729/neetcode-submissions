from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # pass 1 - create frequency table
        # pass 2 - create array of lists (i = count)
        # pass 3 - reverse traversal of array

        counts = defaultdict(int)
        freq = [[] for _ in range(len(nums)+1)]
        res = []

        for num in nums:
            counts[num] += 1

        for key, value in counts.items():
            freq[value].append(key)

        for ptr in range(len(freq) -1, 0, -1):
            for el in freq[ptr]:
                res.append(el)
                if len(res) == k:
                    return res
        
