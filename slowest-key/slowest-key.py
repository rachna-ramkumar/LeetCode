class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        return max([(releaseTimes[0], keysPressed[0])]+[(releaseTimes[i]-releaseTimes[i-1],keysPressed[i]) for i in range(1, len(releaseTimes))])[1]
        