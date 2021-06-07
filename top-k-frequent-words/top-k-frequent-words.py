class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]: 
        hashmap = defaultdict(int)
        for i in words:
            hashmap[i] += 1
            
        result = [[k,v] for k,v in hashmap.items()]
        result.sort()
        result.sort(key = lambda item: item[1], reverse = True)
        return [item[0] for item in result][:k]
        