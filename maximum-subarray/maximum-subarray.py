class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currentSubarray = maxSubarray = nums[0]
        for num in nums[1:]:
            currentSubarray = max(num, currentSubarray + num)
            maxSubarray = max(maxSubarray, currentSubarray)
        return maxSubarray
        
        
        