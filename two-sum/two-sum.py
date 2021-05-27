class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #Brute Force Approach
        '''for i in range(len(nums)):
            j = i + 1
            for j in range(len(nums)):
                if nums[j] == target - nums[i]:
                    return [i,j]'''
        #Time Complexity : O(n^2) | Space Complexity : O(1)
        '''-------------------------------------------------------------------------------------------------------'''
        #Hash Table Approach
        #Two Pass Hash Table
        '''hashmap = {}
        for i in range(len(nums)):
            hashmap[nums[i]] = i
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap and hashmap[complement] != i:
                return [i, hashmap[complement]]'''
        #Time Complexity : O(n) | Space Complexity : O(n)
        '''-------------------------------------------------------------------------------------------------------'''
        #Hash Table Approach
        #Two Pass Hash Table
        hashmap = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap:
                return [i, hashmap[complement]]
            hashmap[nums[i]] = i
        #Time Complexity : O(n) | Space Complexity : O(n)