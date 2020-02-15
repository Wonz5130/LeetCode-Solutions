class Solution:
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        import collections  # 需要导入collections
        count = collections.Counter(s).most_common()  # Counter类就能统计每个字符出现的次数, 使用most_common函数就能按次序排列
        res = ''
        for char, cnt in count:
            res += char*cnt  # 字符与次数相乘
        return res
        # return ''.join(c*-n for n,c in sorted((-s.count(c),c)for c in set(s)))  # 一行代码也能解决
   

if __name__ == "__main__":
    s = "abcc"
    print(Solution().frequencySort(s))