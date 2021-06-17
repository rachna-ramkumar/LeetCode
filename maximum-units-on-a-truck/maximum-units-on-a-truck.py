class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key = lambda x: -x[1])
        currentSize = 0
        maxUnits = 0
        for box, unit in boxTypes:
            if currentSize < truckSize:
                maxUnits += unit * min(truckSize - currentSize, box)
                currentSize += min(truckSize - currentSize, box)
                
        return maxUnits
        