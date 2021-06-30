class Solution:
    def minWindow(self, s, t):
        needed = collections.Counter(t)
        missing = len(t)
        i = left = right = 0
        for j, c in enumerate(s, 1):
            missing -= needed[c] > 0
            needed[c] -= 1
            if not missing:
                while i < j and needed[s[i]] < 0:
                    needed[s[i]] += 1
                    i += 1
                if not right or j - i <= right - left:
                    left, right = i, j
        return s[left:right]