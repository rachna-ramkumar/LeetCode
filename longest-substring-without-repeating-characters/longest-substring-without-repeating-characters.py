class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        window = set()
        longest = 0
        n = len(s)
        while right < n:
            if s[right] in window:
                window.remove(s[left])
                left += 1
            else:
                window.add(s[right])
                right += 1
            longest = max(longest, right - left)
        return longest
                

        
        