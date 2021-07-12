class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewels = set(jewels)
        count = 0
        for each in stones:
            if each in jewels:
                count += 1
        return count
        