class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        diagonals = defaultdict(list)
        for row in range(m):
            for col in range(n):
                diagonals[row - col].append(mat[row][col])
        for diagonal in diagonals.values():
            heapq.heapify(diagonal)
        
        for row in range(m):
            for col in range(n):
                value = heapq.heappop(diagonals[row - col])
                mat[row][col] = value
        return mat