class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        best_ans = sum(nums[:3])
        for i in range(n-2):
            j = i+1
            k = n-1
            while j<k:
                curr_ans = nums[i] + nums[j] + nums[k]
                if abs(curr_ans-target) < abs(best_ans-target):
                    best_ans = curr_ans
                if curr_ans == target:
                    return curr_ans
                elif curr_ans < target:
                    j+=1
                else:
                    k-=1
        return best_ans
            
        