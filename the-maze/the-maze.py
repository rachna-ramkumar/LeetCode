class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        visited = set()
        def recurse(start, visited):
            if tuple(start) in visited:
                return False
            if start == destination:
                return True
            row, col = start
            visited.add(tuple(start))
            for r, c in [(0,1), (0,-1), (1,0), (-1, 0)]:
                nr, nc = row + r, col + c
                while nr >= 0 and nr < len(maze) and nc >=0 and nc < len(maze[0]) and maze[nr][nc] != 1 :
                    nr, nc = nr + r, nc + c
                if recurse([nr-r, nc-c], visited):
                    return True
            return False
        
        return recurse(start, visited)