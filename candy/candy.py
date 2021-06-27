class Solution:
    def candy(self, ratings: List[int]) -> int:
        c, d = 0, 1
        n = len(ratings)
        candies = [1] * n
        for i in range(n-1):   
            if ratings[c]<ratings[d] and candies[d]<=candies[c]:
                candies[d]=candies[c]+1
            c+=1
            d+=1
        c,d=-1,-2
        for i in range(n-1):                 
            if ratings[c]<ratings[d] and candies[d]<=candies[c]:
                candies[d]=candies[c]+1
            c-=1
            d-=1
            
        return sum(candies)