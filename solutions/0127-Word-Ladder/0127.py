from typing import List

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # solution one: BFS
        wordDict = set(wordList)  # no duplicates in the word list
        if endWord not in wordDict:
            return 0
        
        q, visited = [(beginWord, 1)], set()
        while q:
            word, step = q.pop(0)
            if word not in visited:
                visited.add(word)
                if word == endWord:
                    return step
                for i in range(len(word)):
                    for j in "abcdefghijklmnopqrstuvwxyz":  # 26 directions
                        temp = word[:i] + j + word[i+1:]
                        if temp in wordDict and temp not in visited:  # different ways from beginWord to endWord
                            q.append((temp, step + 1))
        return 0

        # solution two: Double BFS
        wordDict, step = set(wordList), 1
        if endWord not in wordDict:
            return 0
        start, end = set([beginWord]), set([endWord])
        while start:
            stack = set([])
            wordDict -= start

            for s in start:
                for i in range(len(beginWord)):
                    for j in string.ascii_lowercase:  # a-z
                        temp = s[:i] + j + s[i+1:]
                        if temp not in wordDict:
                            continue
                        if temp in end:
                            return step + 1
                        stack.add(temp)
            if len(stack) < len(end):
                start = stack
            else:
                start, end = end, stack
            step += 1
        return 0

if __name__ == "__main__":
    beginWord = "hit",
    endWord = "cog",
    wordList = ["hot","dot","dog","lot","log","cog"]
    print(Solution().ladderLength(beginWord, endWord, wordList))