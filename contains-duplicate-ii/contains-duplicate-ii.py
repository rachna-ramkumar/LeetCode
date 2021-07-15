class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        map = set()
        for i in range(len(nums)):
            if nums[i] in map:
                return True
            map.add(nums[i])
            if len(map) > k:
                map.remove(nums[i-k])
        return False
            