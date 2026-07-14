from collections import defaultdict

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        change = defaultdict(int)
        for bill in bills:
            change[bill] += 1
            change_needed = bill - 5
            while change_needed >= 5:
                if change_needed >= 20 and change[20]:
                    change_needed -= 20
                    change[20] -= 1
                elif change_needed >= 10 and change[10]:
                    change_needed -= 10
                    change[10] -= 1
                elif change_needed >= 5 and change[5]:
                    change_needed -= 5
                    change[5] -= 1
                else:
                    return False
        return True