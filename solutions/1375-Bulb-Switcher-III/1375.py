from typing import List

class Solution:
    def numTimesAllBlue(self, light: List[int]) -> int:
        n = len(light)
        flag = [False] * (n+1)
        cnt_blue, cnt_light = 0, 0
        max_i = 0
        for i in range(n):
            flag[light[i]] = True  # turn on bulb开灯
            cnt_light += 1
            max_i = max(max_i, light[i])
            # 已开灯数量 = 当前记录的右边界：灯变蓝计数 + 1
            if cnt_light == max_i:
                cnt_blue += 1
        return cnt_blue

if __name__ == "__main__":
    light = [1,2,3,4,5,6]
    print(Solution().numTimesAllBlue(light))  