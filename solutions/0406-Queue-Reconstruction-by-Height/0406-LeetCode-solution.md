> LeetCode 0406. Queue Reconstruction by Height根据身高重建队列【Medium】【Python】【贪心】

### Problem

[LeetCode](https://leetcode.com/problems/queue-reconstruction-by-height/)

Suppose you have a random list of people standing in a queue. Each person is described by a pair of integers `(h, k)`, where `h` is the height of the person and `k` is the number of people in front of this person who have a height greater than or equal to `h`. Write an algorithm to reconstruct the queue.

**Note:**
The number of people is less than 1,100.

**Example**

```
Input:
[[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]

Output:
[[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]
```

### 问题

[力扣](https://leetcode-cn.com/problems/queue-reconstruction-by-height/)

假设有打乱顺序的一群人站成一个队列。 每个人由一个整数对 `(h, k)` 表示，其中 `h` 是这个人的身高，`k` 是排在这个人前面且身高大于或等于 `h` 的人数。 编写一个算法来重建这个队列。

**注意：**
总人数少于1100人。

**示例**

```
输入:
[[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]

输出:
[[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]
```

### 思路

**贪心**

首先按照身高 h 从高到低，k 从小到大排序。

然后只需插入即可，可以看代码注释。

这里拿示例来举例：

```
输入：
[[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]

排序：
[[7,0], [7,1], [6,1], [5,0], [5,2], [4,4]]

比如[6,1]，表示前面比 6 高的只有一个，那么自然就插入到位置1（从0开始数）：
[[7,0], [6,1], [7,1], [5,0], [5,2], [4,4]]

以此类推

[5,0]：
[[5,0], [7,0], [6,1], [7,1], [5,2], [4,4]]

[5,2]：
[[5,0], [7,0], [5,2], [6,1], [7,1], [4,4]]

[4,4]：
[[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]

end
```

**时间复杂度**: O(len(people))
**空间复杂度**: O(1)

### Python代码

```python
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
```

### 代码地址

[GitHub链接](https://github.com/Wonz5130/LeetCode-Solutions/blob/master/solutions/0406-Queue-Reconstruction-by-Height/0406.py)