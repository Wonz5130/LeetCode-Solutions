> LeetCode 1366. Rank Teams by Votes通过投票对团队排名【Medium】【Python】【排序】

### Problem

[LeetCode](https://leetcode.com/problems/rank-teams-by-votes/)

In a special ranking system, each voter gives a rank from highest to lowest to all teams participated in the competition.

The ordering of teams is decided by who received the most position-one votes. If two or more teams tie in the first position, we consider the second position to resolve the conflict, if they tie again, we continue this process until the ties are resolved. If two or more teams are still tied after considering all positions, we rank them alphabetically based on their team letter.

Given an array of strings `votes` which is the votes of all voters in the ranking systems. Sort all teams according to the ranking system described above.

Return *a string of all teams* **sorted** by the ranking system.

**Example 1:**

```
Input: votes = ["ABC","ACB","ABC","ACB","ACB"]
Output: "ACB"
Explanation: Team A was ranked first place by 5 voters. No other team was voted as first place so team A is the first team.
Team B was ranked second by 2 voters and was ranked third by 3 voters.
Team C was ranked second by 3 voters and was ranked third by 2 voters.
As most of the voters ranked C second, team C is the second team and team B is the third.
```

**Example 2:**

```
Input: votes = ["WXYZ","XYZW"]
Output: "XWYZ"
Explanation: X is the winner due to tie-breaking rule. X has same votes as W for the first position but X has one vote as second position while W doesn't have any votes as second position. 
```

**Example 3:**

```
Input: votes = ["ZMNAGUEDSJYLBOPHRQICWFXTVK"]
Output: "ZMNAGUEDSJYLBOPHRQICWFXTVK"
Explanation: Only one voter so his votes are used for the ranking.
```

**Example 4:**

```
Input: votes = ["BCA","CAB","CBA","ABC","ACB","BAC"]
Output: "ABC"
Explanation: 
Team A was ranked first by 2 voters, second by 2 voters and third by 2 voters.
Team B was ranked first by 2 voters, second by 2 voters and third by 2 voters.
Team C was ranked first by 2 voters, second by 2 voters and third by 2 voters.
There is a tie and we rank teams ascending by their IDs.
```

**Example 5:**

```
Input: votes = ["M","M","M","M"]
Output: "M"
Explanation: Only team M in the competition so it has the first rank.
```

**Constraints:**

- `1 <= votes.length <= 1000`
- `1 <= votes[i].length <= 26`
- `votes[i].length == votes[j].length` for `0 <= i, j < votes.length`.
- `votes[i][j]` is an English **upper-case** letter.
- All characters of `votes[i]` are unique.
- All the characters that occur in `votes[0]` **also occur** in `votes[j]` where `1 <= j < votes.length`.

### 问题

[力扣](https://leetcode-cn.com/problems/rank-teams-by-votes/)

现在有一个特殊的排名系统，依据参赛团队在投票人心中的次序进行排名，每个投票者都需要按从高到低的顺序对参与排名的所有团队进行排位。

排名规则如下：

* 参赛团队的排名次序依照其所获「排位第一」的票的多少决定。如果存在多个团队并列的情况，将继续考虑其「排位第二」的票的数量。以此类推，直到不再存在并列的情况。
* 如果在考虑完所有投票情况后仍然出现并列现象，则根据团队字母的字母顺序进行排名。

给你一个字符串数组 `votes` 代表全体投票者给出的排位情况，请你根据上述排名规则对所有参赛团队进行排名。

请你返回能表示按排名系统 **排序后** 的所有团队排名的字符串。

**示例 1：**

```
输入：votes = ["ABC","ACB","ABC","ACB","ACB"]
输出："ACB"
解释：A 队获得五票「排位第一」，没有其他队获得「排位第一」，所以 A 队排名第一。
B 队获得两票「排位第二」，三票「排位第三」。
C 队获得三票「排位第二」，两票「排位第三」。
由于 C 队「排位第二」的票数较多，所以 C 队排第二，B 队排第三。
```

**示例 2：**

```\
输入：votes = ["WXYZ","XYZW"]
输出："XWYZ"
解释：X 队在并列僵局打破后成为排名第一的团队。X 队和 W 队的「排位第一」票数一样，但是 X 队有一票「排位第二」，而 W 没有获得「排位第二」。 
```

**示例 3：**

```
输入：votes = ["ZMNAGUEDSJYLBOPHRQICWFXTVK"]
输出："ZMNAGUEDSJYLBOPHRQICWFXTVK"
解释：只有一个投票者，所以排名完全按照他的意愿。
```

**示例 4：**

```
输入：votes = ["BCA","CAB","CBA","ABC","ACB","BAC"]
输出："ABC"
解释： 
A 队获得两票「排位第一」，两票「排位第二」，两票「排位第三」。
B 队获得两票「排位第一」，两票「排位第二」，两票「排位第三」。
C 队获得两票「排位第一」，两票「排位第二」，两票「排位第三」。
完全并列，所以我们需要按照字母升序排名。
```

**示例 5：**

```
输入：votes = ["M","M","M","M"]
输出："M"
解释：只有 M 队参赛，所以它排名第一。
```

**提示：**

- `1 <= votes.length <= 1000`
- `1 <= votes[i].length <= 26`
- `votes[i].length == votes[j].length` for `0 <= i, j < votes.length`.
- `votes[i][j]` 是英文 **大写** 字母
- `votes[i]` 中的所有字母都是唯一的
- `votes[0]` 中出现的所有字母 **同样也** 出现在 `votes[j]` 中，其中 `1 <= j < votes.length`

### 思路

**排序**

```
创建一个二维数组 score[26][n+1]。
拿示例一举例：
score[0][0]：表示 A 队排位第一的票数。
score[0][1]：表示 A 队排位第二的票数。
...
score[0][-1]：表示 A 队的编号，排序基于这个。
然后降序排序，最后数字转换成字母就好了。
```

**时间复杂度:** O(m\*n)，m 是投票人个数，n 是参赛队伍数量 。
**空间复杂度:** O(26\*(n + 1))，n 是参赛队伍数量 。

##### Python3代码

```python
class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        n = len(votes[0])
        # create score[26][n+1]
        score = [[0 for i in range(n+1)] for x in range(26)]
        for vote in votes:
            for i, v in enumerate(vote):
                score[ord(v) - ord("A")][i] += 1
                score[ord(v) - ord("A")][-1] = ord("Z") - ord(v) + 1  # A:26 B:25 ··· sort based on it
        score.sort(reverse=True)
        ans = ""
        for i in range(26):
            if score[i][-1] != 0:
                ans += chr(26 - score[i][-1] + 65)  # int to char
        return ans
```

### 代码地址

[GitHub链接](https://github.com/Wonz5130/LeetCode-Solutions/blob/master/solutions/1366-Rank-Teams-by-Votes/1366.py)

### 参考

[coder233 题解](https://leetcode-cn.com/problems/rank-teams-by-votes/solution/pai-xu-by-coder233/263056/)