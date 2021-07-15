class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        map = set()
        for num in nums:
            if num in map:
                return True
            map.add(num)
        return False
        