> LeetCode 0914. X of a Kind in a Deck of Cards卡牌分组【Easy】【Python】【数学】

### Problem

[LeetCode](https://leetcode.com/problems/x-of-a-kind-in-a-deck-of-cards/)

In a deck of cards, each card has an integer written on it.

Return `true` if and only if you can choose `X >= 2` such that it is possible to split the entire deck into 1 or more groups of cards, where:

- Each group has exactly `X` cards.
- All the cards in each group have the same integer.

**Example 1:**

```
Input: deck = [1,2,3,4,4,3,2,1]
Output: true
Explanation: Possible partition [1,1],[2,2],[3,3],[4,4].
```

**Example 2:**

```
Input: deck = [1,1,1,2,2,2,3,3]
Output: false´
Explanation: No possible partition.
```

**Example 3:**

```
Input: deck = [1]
Output: false
Explanation: No possible partition.
```

**Example 4:**

```
Input: deck = [1,1]
Output: true
Explanation: Possible partition [1,1].
```

**Example 5:**

```
Input: deck = [1,1,2,2,2,2]
Output: true
Explanation: Possible partition [1,1],[2,2],[2,2].
```

**Constraints:**

- `1 <= deck.length <= 10^4`
- `0 <= deck[i] < 10^4`

### 问题

[力扣](https://leetcode-cn.com/problems/x-of-a-kind-in-a-deck-of-cards/)

给定一副牌，每张牌上都写着一个整数。

此时，你需要选定一个数字 X，使我们可以将整副牌按下述规则分成 1 组或更多组：

* 每组都有 X 张牌。
* 组内所有的牌上都写着相同的整数。

仅当你可选的 X >= 2 时返回 true。

**示例 1：**

```
输入：[1,2,3,4,4,3,2,1]
输出：true
解释：可行的分组是 [1,1]，[2,2]，[3,3]，[4,4]
```

**示例 2：**

```
输入：[1,1,1,2,2,2,3,3]
输出：false
解释：没有满足要求的分组。
```

**示例 3：**

```
输入：[1]
输出：false
解释：没有满足要求的分组。
```

**示例 4：**

```
输入：[1,1]
输出：true
解释：可行的分组是 [1,1]
```

**示例 5：**

```
输入：[1,1,2,2,2,2]
输出：true
解释：可行的分组是 [1,1]，[2,2]，[2,2]
```

**提示：**

* `1 <= deck.length <= 10^4`
* `0 <= deck[i] < 10^4`

### 思路

**数学**

```
直接调用 Python 的 collections 库，Counter 统计。
然后计算所有整数出现次数的最大公约数。
```

##### Python3代码

```python
from typing import List
import collections
import math

class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        # Counter统计出来是一个字典
        c = list(collections.Counter(deck).values())
        res = c[0]
        # 求所有数的最大公约数
        for x in c:
            res = math.gcd(res, x)
        return res > 1
```

### GitHub链接

[Python](https://github.com/Wonz5130/LeetCode-Solutions/blob/master/solutions/0914-X-of-a-Kind-in-a-Deck-of-Cards/0914.py)