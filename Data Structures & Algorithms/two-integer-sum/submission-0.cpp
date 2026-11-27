class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> mMap;
        vector<int> res;
        for(int i = 0; i < nums.size(); i++) {
            int complement = target - nums[i];
            if(mMap.count(complement)) {
                res = {mMap[complement], i};
            }
            mMap[nums[i]] = i;
        }
        return res;
    }
};
