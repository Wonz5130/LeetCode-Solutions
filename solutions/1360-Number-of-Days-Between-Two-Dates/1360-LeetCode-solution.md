> LeetCode 1360. Number of Days Between Two Dates日期之间隔几天【Easy】【Python】【数学】

### Problem

[LeetCode](https://leetcode.com/problems/number-of-days-between-two-dates/)

Write a program to count the number of days between two dates.

The two dates are given as strings, their format is `YYYY-MM-DD` as shown in the examples.

**Example 1:**

```
Input: date1 = "2019-06-29", date2 = "2019-06-30"
Output: 1
```

**Example 2:**

```
Input: date1 = "2020-01-15", date2 = "2019-12-31"
Output: 15
```

**Constraints:**

- The given dates are valid dates between the years `1971` and `2100`.

### 问题

[力扣](https://leetcode-cn.com/problems/number-of-days-between-two-dates/)

请你编写一个程序来计算两个日期之间隔了多少天。

日期以字符串形式给出，格式为 `YYYY-MM-DD`，如示例所示。

**示例 1：**

```
输入：date1 = "2019-06-29", date2 = "2019-06-30"
输出：1
```

**示例 2：**

```
输入：date1 = "2020-01-15", date2 = "2019-12-31"
输出：15
```

**提示：**

* 给定的日期是 `1971` 年到 `2100` 年之间的有效日期。

### 思路

**数学**

**解法一:**

```
调用 datetime 库。
```

**解法二:**

```
手动计算日期天数。
```

### Python3代码

**解法一:**
```python
class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        # solution one: datetime
        import datetime
        year1, month1, day1 = date1[0:4], date1[5:7], date1[8:10]
        year2, month2, day2 = date2[0:4], date2[5:7], date2[8:10]
        d1 = datetime.datetime(int(year1), int(month1) , int(day1))   # date1
        d2 = datetime.datetime(int(year2), int(month2) , int(day2))   # date2
        return abs((d1 - d2).days)
```

**解法二:**
```python
class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        # solution two: manual calculation
        y1, m1, d1 = map(int, date1.split('-'))
        y2, m2, d2 = map(int, date2.split('-'))
        months = [0,31,28,31,30,31,30,31,31,30,31,30,31]
        
        # get days from 1971
        def getDays(y, m, d):
            ans = 0
            # calculate years
            for i in range(1971, y):
                if (i % 4 == 0 and i % 100 != 0) or i % 400 == 0:  # leap year
                    ans += 366
                else:
                    ans += 365
            # calculate months
            for i in range(1, m):
                if i == 2:  # February
                    ans += 29 if (y % 4 == 0 and y % 100 != 0) or y % 400 == 0 else 28
                else:
                    ans += months[i]
            return ans + d  # calculate days
        
        days1 = getDays(y1, m1, d1)
        days2 = getDays(y2, m2, d2)
        return abs(days1 - days2)
```

### 代码地址

[GitHub链接](https://github.com/Wonz5130/LeetCode-Solutions/blob/master/solutions/1360-Number-of-Days-Between-Two-Dates/1360.py)