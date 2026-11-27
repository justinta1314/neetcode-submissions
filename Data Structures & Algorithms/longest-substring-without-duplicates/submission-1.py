class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        char_set = set()
        max_length = 0
        for i in range(len(s)):
            while s[i] in char_set:
                char_set.remove(s[left])
                left += 1
            char_set.add(s[i])
            window = i - left + 1
            max_length = max(max_length, window)
        return max_length