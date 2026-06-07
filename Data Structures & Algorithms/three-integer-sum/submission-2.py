class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = set()
        nums.sort()
        print(nums)
        # -4 -1 -1 0 1 2
        for i in range(len(nums)-2):
            l = i+1
            r = len(nums)-1
            while l < r:
                if nums[i] + nums[l] + nums[r] < 0:
                    l += 1
                elif nums[i] + nums[l] + nums[r] > 0:
                    r -= 1
                else:
                    triplets.add((nums[i],nums[l],nums[r]))
                    l += 1
                    r -= 1
        return list(triplets)

            
