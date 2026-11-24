class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> mp; // val -> idx
        int& start = nums[0];
        for (auto& num: nums)
        {
            auto it = mp.find(target - num);
            if (it != mp.end())
            {
                if (&num - &start < it->second)
                    return {static_cast<int>(&num - &start), it->second};
                else
                    return {it->second, static_cast<int>(&num - &start)};
            }
            
            mp[num] = &num - &start;
        }
    }
};
