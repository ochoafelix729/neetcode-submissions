import heapq

class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        happy_string = ""
        counts = {
            'a': a,
            'b': b,
            'c': c
        }
        spaces_remaining = {
            'a': 3,
            'b': 3,
            'c': 3
        }
        
        maxHeap = []
        for ch in counts:
            if counts[ch] > 0:
                heapq.heappush_max(maxHeap, (counts[ch], ch))

        while maxHeap:
            count, ch = heapq.heappop_max(maxHeap)

            if len(happy_string) < 2 or (happy_string[len(happy_string)-2:len(happy_string)] != (ch + ch)):
                happy_string += ch
                count -= 1
                if count > 0:
                    heapq.heappush_max(maxHeap, (count, ch))
            else:
                if not maxHeap:
                    break
                new_count, new_ch = heapq.heappop_max(maxHeap)
                happy_string += new_ch
                new_count -= 1
                if new_count > 0:
                    heapq.heappush_max(maxHeap, (new_count, new_ch))
                heapq.heappush_max(maxHeap, (count, ch))

        return happy_string