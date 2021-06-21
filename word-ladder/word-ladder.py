class Solution:
    from collections import deque
    from string import ascii_letters
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        words = set(wordList)
        queue = deque([beginWord])
        distance = 1
        while len(queue) > 0:
            n = len(queue)
            distance += 1
            for i in range(n):
                word = queue.popleft()
                for i in range(len(word)):
                    for c in ascii_letters:
                        nextWord = word[:i] + c + word[i+1 :]
                        if nextWord not in words:
                            continue
                        if nextWord == endWord:
                            return distance
                        queue.append(nextWord)
                        words.remove(nextWord)
        return 0
        