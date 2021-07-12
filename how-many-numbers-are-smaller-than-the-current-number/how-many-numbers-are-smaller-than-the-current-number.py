class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sorted_nums = sorted(nums)
        ans=[]
        for i in nums:
            ans.append(sorted_nums.index(i))
        
        return ans
        