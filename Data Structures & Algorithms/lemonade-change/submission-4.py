from collections import defaultdict

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        fives, tens = 0, 0 # 20-dollar bills will never be used for change
        for bill in bills:
            if bill == 5:
                fives += 1
            elif bill == 10:
                tens += 1

            change_needed = bill - 5

            while tens and change_needed >= 10:
                change_needed -= 10
                tens -= 1
            
            while fives and change_needed >= 5:
                change_needed -= 5
                fives -= 1
            
            if change_needed:
                return False
            
        return True