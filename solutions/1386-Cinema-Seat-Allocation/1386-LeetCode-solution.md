> LeetCode 1386. Cinema Seat Allocation安排电影院座位【Medium】【Python】【哈希表】

### Problem

[LeetCode](https://leetcode.com/problems/cinema-seat-allocation/)

![](https://cdn.jsdelivr.net/gh/Wonz5130/My-Private-ImgHost/img/cinema_seats_1.png)

A cinema has `n` rows of seats, numbered from 1 to `n` and there are ten seats in each row, labelled from 1 to 10 as shown in the figure above.

Given the array `reservedSeats` containing the numbers of seats already reserved, for example, `reservedSeats[i]=[3,8]` means the seat located in row **3** and labelled with **8** is already reserved. 

*Return the maximum number of four-person families you can allocate on the cinema seats.* A four-person family occupies fours seats **in one row**, that are **next to each other**. Seats across an aisle (such as [3,3] and [3,4]) are not considered to be next to each other, however, It is permissible for the four-person family to be separated by an aisle, but in that case, **exactly two people** have to sit on each side of the aisle.

**Example 1:**

![](https://cdn.jsdelivr.net/gh/Wonz5130/My-Private-ImgHost/img/cinema_seats_3.png)

```
Input: n = 3, reservedSeats = [[1,2],[1,3],[1,8],[2,6],[3,1],[3,10]]
Output: 4
Explanation: The figure above shows the optimal allocation for four families, where seats mark with blue are already reserved and contiguous seats mark with orange are for one family. 
```

**Example 2:**

```
Input: n = 2, reservedSeats = [[2,1],[1,8],[2,6]]
Output: 2
```

**Example 3:**

```
Input: n = 4, reservedSeats = [[4,3],[1,4],[4,6],[1,7]]
Output: 4
```

**Constraints:**

- `1 <= n <= 10^9`
- `1 <= reservedSeats.length <= min(10*n, 10^4)`
- `reservedSeats[i].length == 2`
- `1 <= reservedSeats[i][0] <= n`
- `1 <= reservedSeats[i][1] <= 10`
- All `reservedSeats[i]` are distinct.

### 问题

[力扣](https://leetcode-cn.com/problems/cinema-seat-allocation/)

![](https://cdn.jsdelivr.net/gh/Wonz5130/My-Private-ImgHost/img/cinema_seats_1.png)

如上图所示，电影院的观影厅中有 n 行座位，行编号从 1 到 n ，且每一行内总共有 10 个座位，列编号从 1 到 10 。

给你数组 reservedSeats ，包含所有已经被预约了的座位。比如说，researvedSeats[i]=[3,8] ，它表示第 3 行第 8 个座位被预约了。

请你返回 **最多能安排多少个 4 人家庭** 。4 人家庭要占据 **同一行内连续** 的 4 个座位。隔着过道的座位（比方说 [3,3] 和 [3,4]）不是连续的座位，但是如果你可以将 4 人家庭拆成过道两边各坐 2 人，这样子是允许的。

**示例 1：**

![](https://cdn.jsdelivr.net/gh/Wonz5130/My-Private-ImgHost/img/cinema_seats_3.png)

```
输入：n = 3, reservedSeats = [[1,2],[1,3],[1,8],[2,6],[3,1],[3,10]]
输出：4
解释：上图所示是最优的安排方案，总共可以安排 4 个家庭。蓝色的叉表示被预约的座位，橙色的连续座位表示一个 4 人家庭。
```

**示例 2：**

```
输入：n = 2, reservedSeats = [[2,1],[1,8],[2,6]]
输出：2
```

**示例 3：**

```
输入：n = 4, reservedSeats = [[4,3],[1,4],[4,6],[1,7]]
输出：4
```

**提示：**

- `1 <= n <= 10^9`
- `1 <= reservedSeats.length <= min(10*n, 10^4)`
- `reservedSeats[i].length == 2`
- `1 <= reservedSeats[i][0] <= n`
- `1 <= reservedSeats[i][1] <= 10`
- 所有 `reservedSeats[i]` 都是互不相同的。

### 思路

**哈希表**

```
正面考虑容易超时/超内存，可以从反面来考虑。
统计出被预约的位置，然后反向筛选一下可以坐的位置。
```

##### Python3代码

```python
from typing import List

class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        left, right, mid = set(), set(), set()
        count = 0
        
        # 统计被预约的位置
        for r, c in reservedSeats:
            if r in left and r in right and r in mid:
                continue
            if c < 6 and c > 1:
                left.add(r)
            if c < 10 and c > 5:
                right.add(r)
            if c < 8 and c > 3:
                mid.add(r)
        for i in (left|right|mid):
            # 预约位置在两边：1 or 10
            if i not in left and i not in right:
                count += 2
            # 预约位置在左边/右边：2 or 3 or 8 or 9
            elif i not in mid:
                count += 1
            # 预约位置在中间：4 or 5 or 6 or 7
            elif i not in left or i not in right:
                count += 1
        # 反向筛选一下，没有被预约的行最多可以坐两家人
        count += 2*(n - len(left|right|mid))
        return count
```

### GitHub链接

[Python](https://github.com/Wonz5130/LeetCode-Solutions/blob/master/solutions/1386-Cinema-Seat-Allocation/1386.py)

### 参考

[Python 反向筛选](https://leetcode-cn.com/problems/cinema-seat-allocation/solution/python-fan-xiang-shai-xuan-by-ch3cook/)