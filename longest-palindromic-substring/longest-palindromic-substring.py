class Solution:
    def longestPalindrome(self, s: str) -> str:
        palindrome = ''
        size = len(s)
        def _is_palindrome(s):
            return s == s[::-1]
        if _is_palindrome(s):
            return s
		# here we do basically the same, but loop over the window size in a reversed way,
		# stopping the search if the next iteration would check shorter strings than we already 
		# have as a valid palindrome. So we avoid some extra loops.
        for step in range(size, -1, -1):
            for curr in range(size):
                start, stop = curr, curr+step+1
                if stop > size or (palindrome and step < len(palindrome)):
                    break
                subs = s[start:stop]
                if _is_palindrome(subs) and len(subs) > len(palindrome):
                    palindrome = subs
        return palindrome