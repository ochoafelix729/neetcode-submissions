class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:

        people.sort()
        l, r = 0, len(people)-1

        boats = 0
        curWeight = 0
        while l <= r:
            # try
            if curWeight + people[r] == limit:
                curWeight = 0
                boats += 1
                r -= 1
            elif curWeight + people[r] + people[l] == limit:
                curWeight = 0
                boats += 1
                r -= 1
                l += 1
            elif curWeight + people[r] + people[l] > limit:
                curWeight = 0
                boats += 1
                r -= 1
            else:
                curWeight = curWeight + people[l] + people[r]
                l += 1
        
        return boats


            
            
        
        '''
        2 3 4 5 , limit=9



        5 1 4 2 , limit=6
        5 4 2 1
        boat 1: 5
        boat 2: 4,2
        boat 3: 1


        5 1 4 2 , limit=6
        1 2 4 5
        ^     ^
        1 2 4 5
          ^ ^
        boat 1: 1,5
        boat 2: 2,4

        1 3 2 3 2 , limit=3
        1 2 2 3 3
          ^
        boat 1: 3
        boat 2: 3
        boat 3: 1, 2
        boat 4: 2
        '''