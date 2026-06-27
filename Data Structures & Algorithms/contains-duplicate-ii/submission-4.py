class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if len(nums) == 1:
            return False

        hashset = {nums[0]}
        l = 0
        for r in range(1, len(nums)):
            if nums[r] in hashset:
                return True
            hashset.add(nums[r])
            if r - l >= k:
                hashset.remove(nums[l])
                l += 1
        return False


        # 1 2 3 1
        # 0 1 2 3
        