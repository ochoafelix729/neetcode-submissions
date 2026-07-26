class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # find counts
        # each bucket should be count : list of elements that have that count

        counts = defaultdict(int)
        for num in nums:
            counts[num] += 1
        
        buckets = [[] for _ in range(len(nums)+1)]
        for num, count in counts.items():
            buckets[count].append(num)
        res = []
        i = len(buckets)-1
        while True:
            for num in buckets[i]:
                res.append(num)
                if len(res) == k:
                    return res
            i -= 1

        return res