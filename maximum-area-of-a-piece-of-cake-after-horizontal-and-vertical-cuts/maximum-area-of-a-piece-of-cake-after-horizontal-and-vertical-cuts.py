class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
	    mod = 10 ** 9 + 7
	    horizontalCuts += [0, h]
	    verticalCuts += [0, w]
	    horizontalCuts.sort()
	    verticalCuts.sort()

	    max_h = max(n - p for p, n in zip(horizontalCuts, horizontalCuts[1:]))
	    max_w = max(n - p for p, n in zip(verticalCuts, verticalCuts[1:]))
	    return max_h * max_w % mod