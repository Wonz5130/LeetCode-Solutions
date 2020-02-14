class Solution(object):
    def findLongestWord(self, s, d):
        """
        :type s: str
        :type d: List[str]
        :rtype: str
        """
        res = ""
        max = -1
        for word in d:
            if len(s) < len(word) or len(word) == 0:
                continue
            j = 0  # j 指针判断 word 中的每个字符
            for i in range(len(s)):  # i 指针判断 s 中的每个字符
                if s[i] == word[j]:
                    j += 1  # 如果相等, 只移动 j 指针
                if j == len(word):  # j 指针已移动 word 末尾
                    if len(word) > max:  # 更新 res 和 max
                        res = word
                        max = len(word)
                    elif len(word) == max:
                        res = min(res, word)  # 长度相同则选最小字典序的 word 
                    break
        return res

if __name__ == "__main__":
    s = 'abpcplea'
    d = ['ale', 'apple', 'monkey', 'plea']
    print(Solution().findLongestWord(s,d))