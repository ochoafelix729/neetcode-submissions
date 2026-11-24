class Solution {
public:
    bool containsNearbyDuplicate(vector<int>& nums, int k) {        
        if (k == 0)
            return false;
            
        int l = 0;
        int r = 0;
        unordered_set<int> window;
        for (auto& num : nums)
        {
            if (window.contains(num))
            {
                return true;
            }
            if (abs(r - l) == k)
            {
                window.erase(nums[l]);
                l++;
            }
            window.insert(num);
            r++;
        }
        return false;
    }
};