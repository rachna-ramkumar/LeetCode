class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        map = set(nums)
        out = []
        for num in range(1, len(nums) + 1):
            if num not in map:
                out.append(num)
        return out
        