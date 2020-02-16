class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        people.sort(key = lambda x : (-x[0], x[1]))  # 按照h从高到低，k从小到大排序
        res = []
        for p in people:
            res.insert(p[1], p)  # 每次只要在p[1]位置插入p就行，因为p[1]表示p前只能出现的个数
        return res

if __name__ == "__main__":
    people = [[7,0],[7,1],[6,1],[5,0],[5,2],[4,4]]
    print(Solution().reconstructQueue(people))