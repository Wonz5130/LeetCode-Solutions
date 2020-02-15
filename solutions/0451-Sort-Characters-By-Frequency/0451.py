class Solution:
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        # # 法一：collections.Counter
        # import collections  # 需要导入collections
        # count = collections.Counter(s).most_common()  # Counter类就能统计每个字符出现的次数, 使用most_common函数就能按次序排列
        # res = ''
        # for char, cnt in count:
        #     res += char*cnt  # 字符与次数相乘
        # return res
        
        # 法二：桶排序
        import collections

        # 统计字符个数
        ret = []
        count_frequency = collections.defaultdict(int)
        for i in s:
            count_frequency[i] += 1  # 统计字符个数
        
        # 桶排序
        buckets = [[] for i in range(len(s) + 1)]
        for i in count_frequency:  # i是字符
            # print (i)
            buckets[count_frequency[i]].extend(i * count_frequency[i])
        
        # 打印排完序的字符串
        for i in buckets[::-1]:  # -1表示逆序
            if(i):
                ret.extend(i)
        return ''.join(ret)

        # return ''.join(c*-n for n,c in sorted((-s.count(c),c)for c in set(s)))  # 一行代码也能解决
   

if __name__ == "__main__":
    s = "abcc"
    print(Solution().frequencySort(s))