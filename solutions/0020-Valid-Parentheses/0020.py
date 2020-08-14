class Solution:
    def isValid(self, s: str) -> bool:
        dic = {'}': '{', ']': '[', ')': '('}
        stack = []
        for c in s:
            if stack and c in dic:
                if stack[-1] == dic[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return not stack