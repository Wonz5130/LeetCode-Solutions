from typing import List

class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        p = [x for x in range(1, m + 1)]
        res = []

        for x in queries:
            temp = p.index(x)
            num = p[temp]
            res.append(temp)
            p.remove(p[temp])
            p.insert(0, num)
        return res

if __name__ == "__main__":
    queries = [3,1,2,1]
    m = 5
    queries = [4,1,2,2]
    m = 4
    queries = [7,5,5,8,3]
    m = 8
    print(Solution().processQueries(queries, m))