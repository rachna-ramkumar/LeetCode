class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]: 
        wordCounts = defaultdict(int)
        
        for word in words:
            wordCounts[word] += 1
        
        result = [[k,v] for k, v in wordCounts.items()]
        result.sort()
        result.sort(key = lambda x : x[1], reverse = True)
        
        return [item[0] for item in result][:k]
        