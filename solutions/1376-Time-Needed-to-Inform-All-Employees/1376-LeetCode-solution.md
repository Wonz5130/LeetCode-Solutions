> LeetCode 1376. Time Needed to Inform All Employees通知所有员工所需的时间【Medium】【Python】【自底向上遍历】

### Problem

[LeetCode](https://leetcode.com/problems/time-needed-to-inform-all-employees/)

A company has `n` employees with a unique ID for each employee from `0` to `n - 1`. The head of the company has is the one with `headID`.

Each employee has one direct manager given in the `manager` array where `manager[i]` is the direct manager of the `i-th` employee, `manager[headID] = -1`. Also it's guaranteed that the subordination relationships have a tree structure.

The head of the company wants to inform all the employees of the company of an urgent piece of news. He will inform his direct subordinates and they will inform their subordinates and so on until all employees know about the urgent news.

The `i-th` employee needs `informTime[i]` minutes to inform all of his direct subordinates (i.e After informTime[i] minutes, all his direct subordinates can start spreading the news).

Return *the number of minutes* needed to inform all the employees about the urgent news.

**Example 1:**

```
Input: n = 1, headID = 0, manager = [-1], informTime = [0]
Output: 0
Explanation: The head of the company is the only employee in the company.
```

**Example 2:**

![](https://cdn.jsdelivr.net/gh/Wonz5130/My-Private-ImgHost/img/graph.png)

```
Input: n = 6, headID = 2, manager = [2,2,-1,2,2,2], informTime = [0,0,1,0,0,0]
Output: 1
Explanation: The head of the company with id = 2 is the direct manager of all the employees in the company and needs 1 minute to inform them all.
The tree structure of the employees in the company is shown.
```

**Example 3:**

![](https://cdn.jsdelivr.net/gh/Wonz5130/My-Private-ImgHost/img/1730_example_3_5.png)

```
Input: n = 7, headID = 6, manager = [1,2,3,4,5,6,-1], informTime = [0,6,5,4,3,2,1]
Output: 21
Explanation: The head has id = 6. He will inform employee with id = 5 in 1 minute.
The employee with id = 5 will inform the employee with id = 4 in 2 minutes.
The employee with id = 4 will inform the employee with id = 3 in 3 minutes.
The employee with id = 3 will inform the employee with id = 2 in 4 minutes.
The employee with id = 2 will inform the employee with id = 1 in 5 minutes.
The employee with id = 1 will inform the employee with id = 0 in 6 minutes.
Needed time = 1 + 2 + 3 + 4 + 5 + 6 = 21.
```

**Example 4:**

```
Input: n = 15, headID = 0, manager = [-1,0,0,1,1,2,2,3,3,4,4,5,5,6,6], informTime = [1,1,1,1,1,1,1,0,0,0,0,0,0,0,0]
Output: 3
Explanation: The first minute the head will inform employees 1 and 2.
The second minute they will inform employees 3, 4, 5 and 6.
The third minute they will inform the rest of employees.
```

**Example 5:**

```
Input: n = 4, headID = 2, manager = [3,3,-1,2], informTime = [0,0,162,914]
Output: 1076
```

**Constraints:**

- `1 <= n <= 10^5`
- `0 <= headID < n`
- `manager.length == n`
- `0 <= manager[i] < n`
- `manager[headID] == -1`
- `informTime.length == n`
- `0 <= informTime[i] <= 1000`
- `informTime[i] == 0` if employee `i` has no subordinates.
- It is **guaranteed** that all the employees can be informed.

### 问题

[力扣](https://leetcode-cn.com/problems/time-needed-to-inform-all-employees/)

公司里有 n 名员工，每个员工的 ID 都是独一无二的，编号从 0 到 n - 1。公司的总负责人通过 headID 进行标识。

在 manager 数组中，每个员工都有一个直属负责人，其中 manager[i] 是第 i 名员工的直属负责人。对于总负责人，manager[headID] = -1。题目保证从属关系可以用树结构显示。

公司总负责人想要向公司所有员工通告一条紧急消息。他将会首先通知他的直属下属们，然后由这些下属通知他们的下属，直到所有的员工都得知这条紧急消息。

第 i 名员工需要 informTime[i] 分钟来通知它的所有直属下属（也就是说在 informTime[i] 分钟后，他的所有直属下属都可以开始传播这一消息）。

返回通知所有员工这一紧急消息所需要的 **分钟数** 。

**示例 1：**

```
输入：n = 1, headID = 0, manager = [-1], informTime = [0]
输出：0
解释：公司总负责人是该公司的唯一一名员工。
```

**示例 2：**

![](https://cdn.jsdelivr.net/gh/Wonz5130/My-Private-ImgHost/img/graph.png)

```
输入：n = 6, headID = 2, manager = [2,2,-1,2,2,2], informTime = [0,0,1,0,0,0]
输出：1
解释：id = 2 的员工是公司的总负责人，也是其他所有员工的直属负责人，他需要 1 分钟来通知所有员工。
上图显示了公司员工的树结构。
```

**示例 3：**

![](https://cdn.jsdelivr.net/gh/Wonz5130/My-Private-ImgHost/img/1730_example_3_5.png)

```
输入：n = 7, headID = 6, manager = [1,2,3,4,5,6,-1], informTime = [0,6,5,4,3,2,1]
输出：21
解释：总负责人 id = 6。他将在 1 分钟内通知 id = 5 的员工。
id = 5 的员工将在 2 分钟内通知 id = 4 的员工。
id = 4 的员工将在 3 分钟内通知 id = 3 的员工。
id = 3 的员工将在 4 分钟内通知 id = 2 的员工。
id = 2 的员工将在 5 分钟内通知 id = 1 的员工。
id = 1 的员工将在 6 分钟内通知 id = 0 的员工。
所需时间 = 1 + 2 + 3 + 4 + 5 + 6 = 21 。
```

**示例 4：**

```
输入：n = 15, headID = 0, manager = [-1,0,0,1,1,2,2,3,3,4,4,5,5,6,6], informTime = [1,1,1,1,1,1,1,0,0,0,0,0,0,0,0]
输出：3
解释：第一分钟总负责人通知员工 1 和 2 。
第二分钟他们将会通知员工 3, 4, 5 和 6 。
第三分钟他们将会通知剩下的员工。
```

**示例 5：**

```
输入：n = 4, headID = 2, manager = [3,3,-1,2], informTime = [0,0,162,914]
输出：1076
```

**提示：**

- `1 <= n <= 10^5`
- `0 <= headID < n`
- `manager.length == n`
- `0 <= manager[i] < n`
- `manager[headID] == -1`
- `informTime.length == n`
- `0 <= informTime[i] <= 1000`
- 如果员工 `i` 没有下属，`informTime[i] == 0` 。
- 题目 **保证** 所有员工都可以收到通知。

### 思路

**自底向上遍历**

```
自底向上，每次加上该层员工所需的通知时间，再逐层到上一层负责人。
```

##### Python3代码

```python
class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        res = 0
        for i in range(len(manager)):
            # 剪枝
            if informTime[i] == 0:
                temp = 0
                index = i
                # 自底向上遍历
                while index != -1:
                    temp += informTime[index]
                    index = manager[index]
                res = max(res, temp)
        return res
```

### 代码地址

[GitHub链接](https://github.com/Wonz5130/LeetCode-Solutions/blob/master/solutions/1376-Time-Needed-to-Inform-All-Employees/1376.py)