from collections import defaultdict
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        map = defaultdict(int)
        for i in nums:
            map[i] += 1
        for i in map:
            if map[i] == 1:
                return i