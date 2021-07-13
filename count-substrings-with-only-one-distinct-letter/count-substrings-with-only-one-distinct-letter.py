class Solution:
    def countLetters(self, s: str) -> int:
        n = len(s)
        total = [1] * n
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                total[i] = total[i - 1] + 1
        return sum(total)
            
        