class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> mMap;
        for(int i = 0; i < nums.size(); i++) {
            int complement = target - nums[i];
            if(mMap.contains(complement)) {
                return {mMap[complement], i};
            }
            mMap[nums[i]] = i;
        }
        return {};
    }
};
