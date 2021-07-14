class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        seen = set()
        out = []
        for i in range(0, len(nums)):
            if nums[i] in seen:
                out.append(nums[i])
            seen.add(nums[i])
        return out
        