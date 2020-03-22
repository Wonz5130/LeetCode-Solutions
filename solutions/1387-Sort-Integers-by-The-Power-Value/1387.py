class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        nums, weight = [], []
        for x in range(lo, hi + 1):
            nums.append(x)
            weight.append(self.step(x))
        # 将两个列表合并成字典
        dic = dict(zip(nums, weight))
        
        # 先根据权重排序，再根据数值排序
        res = sorted(dic.items(), key=lambda x: (x[1],x[0]))
        return res[k-1][0]
    
    def step(self, x):
        cnt = 0
        if x == 1:
            return cnt
        while x != 1:
            if x % 2:
                x = 3 * x + 1
            else:
                x = x / 2
            cnt += 1
        return cnt

if __name__ == "__main__":
    lo = 12
    hi = 15
    k = 2
    print(Solution().getKth(lo, hi, k))