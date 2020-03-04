> LeetCode 0017. Letter Combinations of a Phone Number电话号码的字母组合【Medium】【Python】【回溯】【DFS】【暴力】

### Problem

[LeetCode](https://leetcode.com/problems/letter-combinations-of-a-phone-number/)

Given a string containing digits from `2-9` inclusive, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

![](https://cdn.jsdelivr.net/gh/Wonz5130/My-Private-ImgHost/img/200px-Telephone-keypad2.svg.png)

**Example:**

```
Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
```

**Note:**

Although the above answer is in lexicographical order, your answer could be in any order you want.

### 问题

[力扣](https://leetcode-cn.com/problems/letter-combinations-of-a-phone-number/submissions/)

给定一个仅包含数字 `2-9` 的字符串，返回所有它能表示的字母组合。

给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。

![](https://cdn.jsdelivr.net/gh/Wonz5130/My-Private-ImgHost/img/200px-Telephone-keypad2.svg.png)

**示例:**

```
输入："23"
输出：["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
```

**说明:**
尽管上面的答案是按字典序排列的，但是你可以任意选择答案输出的顺序。

### 思路

##### 解法一

**回溯 DFS**

```
注意要判断 path != ''，因为当 digits = ''，返回的是 [] 不是 ['']。
```

##### Python3代码

```python
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # solution one: backtracking
        kbmaps = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        ans = []
        self.dfs(digits, 0, ans, '', kbmaps)
        return ans
    
    def dfs(self, string, index, ans, path, kbmaps):
        if index == len(string):
            if path != '':  # while digits = '', return [] not ['']
                ans.append(path)
            return
        for i in kbmaps[string[index]]:
            self.dfs(string, index + 1, ans, path + i, kbmaps)
```

##### 解法二

**暴力**

##### Python3代码

```python
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # solution two: brute force search
        if digits == "":
            return []
        d = {'2' : "abc", '3' : "def", '4' : "ghi", '5' : "jkl", '6' : "mno", '7' : "pqrs", '8' : "tuv", '9' : "wxyz"}
        ans = ['']
        for x in digits:
            ans = [y + c for c in d[x] for y in ans]
        return ans
```

### 代码地址

[GitHub链接](https://github.com/Wonz5130/LeetCode-Solutions/blob/master/solutions/0017-Letter-Combinations-of-a-Phone-Number/0017.py)