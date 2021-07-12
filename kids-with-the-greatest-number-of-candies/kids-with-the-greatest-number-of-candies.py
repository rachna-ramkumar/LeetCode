class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxCandies = max(candies)
        
        return [ (x + extraCandies) >= maxCandies for x in candies]
                
        
        