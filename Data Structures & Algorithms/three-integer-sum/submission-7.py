class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        numsMap = {} # num -> index
        res = set()
        for i in range(len(nums)):
            for j in range((len(nums))):
                if nums[j] not in numsMap:
                    numsMap[nums[j]] = j
                if j == i:
                    continue
                if (-1 * (nums[i] + nums[j])) in numsMap:
                    num = -1 * (nums[i] + nums[j])
                    if numsMap[num] != i and numsMap[num] != j:
                        res.add(tuple(sorted([nums[i], nums[j], num])))
        return list(res)