class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # 统计元素的频率
        count = dict()
        for num in nums:
            count[num] = count.get(num, 0) + 1  # 返回字典 count 中 num 元素对应的值, 没有就赋值为 0
        
        # 桶排序
        bucket = [[] for i in range(len(nums) + 1)]
        for key, value in count.items():
            bucket[value].append(key)
        
        # 逆序取出前 k 个元素
        res = list()
        for i in range(len(nums), -1, -1):  # 最后一个 -1 表示逆序
            if bucket[i]:
                res.extend(bucket[i])  # 在列表末尾追加元素
            if len(res) >= k:  # 只要前 k 个
                break
        return res[:k]  # 输出第 k 个之前的元素（包括第 k 个元素)

if __name__ == '__main__':
    nums = [4,1,1,1,2,2,3]
    k = 2
    print(Solution().topKFrequent(nums, k))