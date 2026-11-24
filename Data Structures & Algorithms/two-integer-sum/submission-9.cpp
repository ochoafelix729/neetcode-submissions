class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> mp; // val -> idx
        int& start = nums[0];
        for (auto& num: nums)
        {
            if (mp.contains(target - num))
            {
                int idx1 = &num - &start;
                int idx2 = mp[target - num];
                if (idx1 < idx2)
                    return {idx1, idx2};
                else
                    return {idx2, idx1};
            }
            if (!mp.contains(num))
            {
                mp[num] = &num - &start;
            }
        }
    }
};
