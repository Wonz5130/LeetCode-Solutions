> LeetCode 1409. Queries on a Permutation With Key查询带键的排列【Medium】【Python】【模拟】

### Problem

[LeetCode](https://leetcode.com/problems/queries-on-a-permutation-with-key/)

Given the array `queries` of positive integers between `1` and `m`, you have to process all `queries[i]` (from `i=0` to `i=queries.length-1`) according to the following rules:

- In the beginning, you have the permutation `P=[1,2,3,...,m]`.
- For the current `i`, find the position of `queries[i]` in the permutation `P` (**indexing from 0**) and then move this at the beginning of the permutation `P.` Notice that the position of `queries[i]` in `P` is the result for `queries[i]`.

Return an array containing the result for the given `queries`.

**Example 1:**

```
Input: queries = [3,1,2,1], m = 5
Output: [2,1,2,1] 
Explanation: The queries are processed as follow: 
For i=0: queries[i]=3, P=[1,2,3,4,5], position of 3 in P is 2, then we move 3 to the beginning of P resulting in P=[3,1,2,4,5]. 
For i=1: queries[i]=1, P=[3,1,2,4,5], position of 1 in P is 1, then we move 1 to the beginning of P resulting in P=[1,3,2,4,5]. 
For i=2: queries[i]=2, P=[1,3,2,4,5], position of 2 in P is 2, then we move 2 to the beginning of P resulting in P=[2,1,3,4,5]. 
For i=3: queries[i]=1, P=[2,1,3,4,5], position of 1 in P is 1, then we move 1 to the beginning of P resulting in P=[1,2,3,4,5]. 
Therefore, the array containing the result is [2,1,2,1].  
```

**Example 2:**

```
Input: queries = [4,1,2,2], m = 4
Output: [3,1,2,0]
```

**Example 3:**

```
Input: queries = [7,5,5,8,3], m = 8
Output: [6,5,0,7,5]
```

**Constraints:**

- `1 <= m <= 10^3`
- `1 <= queries.length <= m`
- `1 <= queries[i] <= m`

### 问题

[力扣](https://leetcode-cn.com/problems/queries-on-a-permutation-with-key/)

给你一个待查数组 queries ，数组中的元素为 1 到 m 之间的正整数。 请你根据以下规则处理所有待查项 queries[i]（从 i=0 到 i=queries.length-1）：

* 一开始，排列 P=[1,2,3,...,m]。
* 对于当前的 i ，请你找出待查项 queries[i] 在排列 P 中的位置（下标从 0 开始），然后将其从原位置移动到排列 P 的起始位置（即下标为 0 处）。注意， queries[i] 在 P 中的位置就是 queries[i] 的查询结果。

请你以数组形式返回待查数组  queries 的查询结果。

**示例 1：**

```
输入：queries = [3,1,2,1], m = 5
输出：[2,1,2,1] 
解释：待查数组 queries 处理如下：
对于 i=0: queries[i]=3, P=[1,2,3,4,5], 3 在 P 中的位置是 2，接着我们把 3 移动到 P 的起始位置，得到 P=[3,1,2,4,5] 。
对于 i=1: queries[i]=1, P=[3,1,2,4,5], 1 在 P 中的位置是 1，接着我们把 1 移动到 P 的起始位置，得到 P=[1,3,2,4,5] 。 
对于 i=2: queries[i]=2, P=[1,3,2,4,5], 2 在 P 中的位置是 2，接着我们把 2 移动到 P 的起始位置，得到 P=[2,1,3,4,5] 。
对于 i=3: queries[i]=1, P=[2,1,3,4,5], 1 在 P 中的位置是 1，接着我们把 1 移动到 P 的起始位置，得到 P=[1,2,3,4,5] 。 
因此，返回的结果数组为 [2,1,2,1] 。
```

**示例 2：**

```
输入：queries = [4,1,2,2], m = 4
输出：[3,1,2,0]
```

**示例 3：**

```
输入：queries = [7,5,5,8,3], m = 8
输出：[6,5,0,7,5]
```

**提示：**

- `1 <= m <= 10^3`
- `1 <= queries.length <= m`
- `1 <= queries[i] <= m`

### 思路

**模拟**

**时间复杂度:** O(n)，n 为 queries 的长度
**空间复杂度:** O(n)

##### Python3代码

```python
from typing import List

class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        p = [x for x in range(1, m + 1)]
        res = []

        for x in queries:
            temp = p.index(x)
            num = p[temp]
            res.append(temp)
            p.remove(p[temp])
            p.insert(0, num)
        return res
```

### GitHub链接

[Python](https://github.com/Wonz5130/LeetCode-Solutions/blob/master/solutions/1409-Queries-on-a-Permutation-With-Key/1409.py)