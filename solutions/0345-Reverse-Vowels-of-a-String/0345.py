class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        left, right = 0, len(s)-1  # 同时赋值
        vowels = 'aeiou'
        string = list(s)  # 字符串不能改变, 所以要转为 list
        while left < right:
            if string[left].lower() not in vowels:  # lower 是取小写
                left += 1
            elif string[right].lower() not in vowels:
                right -= 1
            else:
                string[left], string[right] = string[right], string[left]
                left += 1
                right -= 1
        return ''.join(string)  # 将 string 中的元素以指定的字符连接生成一个新的字符串
        
if __name__ == "__main__":
    str = "hello"
    print(Solution().reverseVowels(str))