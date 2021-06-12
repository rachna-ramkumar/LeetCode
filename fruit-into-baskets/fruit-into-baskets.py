class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        result = 0        
        l = r = -1
        mem = collections.defaultdict(int)
        
        while r < len(tree):
            while len(mem) <= 2: # valid
                result = max(result, sum(mem.values()))

                r += 1
                if r == len(tree):  return result
                
                mem[tree[r]] += 1
                
            while len(mem) > 2: # solution invalid
                l += 1
                
                mem[tree[l]] -= 1
                if mem[tree[l]] == 0: del mem[tree[l]]
            
        return result
                