from typing import List
import copy

class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        n = len(words)
        res = []
        for i in range(n):
            temp = copy.deepcopy(words)
            temp.remove(words[i])

            for j in range(n - 1):
                if words[i] in temp[j]:
                    res.append(words[i])
        return list(set(res))

if __name__ == "__main__":
    words = ["mass","as","hero","superhero"]
    # words = ["leetcoder","leetcode","od","hamlet","am"]
    print(Solution().stringMatching(words))