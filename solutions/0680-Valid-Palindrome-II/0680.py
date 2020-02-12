class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left, right = 0, len(s)-1  # 同时赋值
        while left <= right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                temp1 = s[:left] + s[left+1:]  # 删掉 s[left] 后的字符, 即字符串拼接: s[0] 到 s[left-1] + s[left+1] 到 s[len(s)-1]
                temp2 = s[:right] + s[right+1:]
                if temp1 == temp1[::-1] or temp2 == temp2[::-1]:  # 判断删掉 s[left] 或者删掉 s[right], s是否为回文, [::-1]是从尾到头逆序遍历
                    return True
                else:
                    return False
        return True

if __name__ == "__main__":
    str = "abca"
    print(Solution().validPalindrome(str))