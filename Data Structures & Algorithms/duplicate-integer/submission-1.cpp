class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        unordered_set<int> freqSet;
        for(int a : nums) {
            if(freqSet.contains(a)) {
                return true;
            }
            freqSet.insert(a);
        }
        return false;
    }
};