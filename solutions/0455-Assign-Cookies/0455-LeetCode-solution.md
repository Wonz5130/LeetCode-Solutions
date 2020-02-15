> LeetCode 0455. Assign Cookies分发饼干【Easy】【Python】【贪心】

### Problem

[LeetCode](https://leetcode.com/problems/assign-cookies/)

Assume you are an awesome parent and want to give your children some cookies. But, you should give each child at most one cookie. Each child i has a greed factor gi, which is the minimum size of a cookie that the child will be content with; and each cookie j has a size sj. If sj >= gi, we can assign the cookie j to the child i, and the child i will be content. Your goal is to maximize the number of your content children and output the maximum number.

**Note:**
You may assume the greed factor is always positive.
You cannot assign more than one cookie to one child.

**Example 1:**

```
Input: [1,2,3], [1,1]

Output: 1

Explanation: You have 3 children and 2 cookies. The greed factors of 3 children are 1, 2, 3. 
And even though you have 2 cookies, since their size is both 1, you could only make the child whose greed factor is 1 content.
You need to output 1.
```

**Example 2:**

```
Input: [1,2], [1,2,3]

Output: 2

Explanation: You have 2 children and 3 cookies. The greed factors of 2 children are 1, 2. 
You have 3 cookies and their sizes are big enough to gratify all of the children, 
You need to output 2.
```

### 问题

[力扣](https://leetcode-cn.com/problems/assign-cookies/)

假设你是一位很棒的家长，想要给你的孩子们一些小饼干。但是，每个孩子最多只能给一块饼干。对每个孩子 i ，都有一个胃口值 gi ，这是能让孩子们满足胃口的饼干的最小尺寸；并且每块饼干 j ，都有一个尺寸 sj 。如果 sj >= gi ，我们可以将这个饼干 j 分配给孩子 i ，这个孩子会得到满足。你的目标是尽可能满足越多数量的孩子，并输出这个最大数值。

**注意：**

你可以假设胃口值为正。
一个小朋友最多只能拥有一块饼干。

**示例 1:**

```
输入: [1,2,3], [1,1]

输出: 1

解释: 
你有三个孩子和两块小饼干，3个孩子的胃口值分别是：1,2,3。
虽然你有两块小饼干，由于他们的尺寸都是1，你只能让胃口值是1的孩子满足。
所以你应该输出1。
```

**示例 2:**

```
输入: [1,2], [1,2,3]

输出: 2

解释: 
你有两个孩子和三块小饼干，2个孩子的胃口值分别是1,2。
你拥有的饼干数量和尺寸都足以让所有孩子满足。
所以你应该输出2.
```

### 思路

**贪心**

先将 `贪婪指数` 和 `饼干大小` 从小到大排完序，然后 i, j 指针分别指向 `贪婪指数` 和 `饼干大小` 的末尾，如果 `贪婪指数` 满足小于等于饼干大小，说明此 `贪婪指数` 可以被满足，于是，计数加 1，j 指针往左移一位。不管 `贪婪指数` 有没有满足，i 指针都要往左移，因为如果满足，那么可以判断下一位，如果不满足，那么自然也不在考虑之中。

**时间复杂度**: O(max(len(g), len(s)))
**空间复杂度**: O(1)

### Python代码

```python
class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        # 贪心
        cnt = 0
        g, s = sorted(g), sorted(s)  # 从小到大排序
        i, j = len(g)-1, len(s)-1  # 指向末尾
        while min(i, j) >= 0:
            if g[i] <= s[j]:  # 贪婪指数要 <= 饼干大小
                cnt += 1
                j -= 1
            i -= 1  # 不管满不满足 size，i 都要往左移一位
        return cnt
```

### 代码地址

[GitHub链接](https://github.com/Wonz5130/LeetCode-Solutions/blob/master/solutions/0455-Assign-Cookies/0455.py)