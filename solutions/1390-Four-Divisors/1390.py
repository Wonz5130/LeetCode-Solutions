from typing import List

class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        sum = 0
        for x in nums:
            if x == 1 or x == 2 or x == 3:
                continue
            num = 2
            temp = [1, x]
            # 计算因数
            while num ** 2 <= x:  # 用 num^2 <= x 比 num <= sqrt(x) 好
                if len(temp) > 4:
                    break
                if not x % num:
                    if num not in temp:
                        temp.append(num)
                    if int(x/num) not in temp:
                        temp.append(int(x/num))
                num += 1
            # print(temp)
            if len(temp) == 4:
                for _ in temp:
                    # print(_)
                    sum += _
        return int(sum)

if __name__ == "__main__":
    nums = [21,4,7]
    print(Solution().sumFourDivisors(nums))