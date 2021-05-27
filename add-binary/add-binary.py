class Solution:
    def addBinary(self, a, b) -> str:
        c = int(a, 2) + int(b, 2)
        return '{0:b}'.format(c)
        
        