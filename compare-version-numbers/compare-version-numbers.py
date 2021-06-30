class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        parts1 = version1.split('.')
        parts2 = version2.split('.')
        p1, p2 = len(parts1), len(parts2)
        
        for i in range(max(p1, p2)):
            i1 = int(parts1[i]) if i < p1 else 0
            i2 = int(parts2[i]) if i < p2 else 0
            if i1 != i2:
                return 1 if i1 > i2 else -1
        return 0
        
    
    
        
        
        
        