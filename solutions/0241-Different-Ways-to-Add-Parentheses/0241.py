from typing import List

class Solution:
    def diffWaysToCompute(self, input: str) -> List[int]:
        if input.isdigit():  # input only contains digital
            return [int(input)]
        n = len(input)
        res = []
        for i in range(n):
            if input[i] in '+-*':
                lefts = self.diffWaysToCompute(input[:i])
                rights = self.diffWaysToCompute(input[i+1:])
                for left in lefts:
                    for right in rights:
                        if input[i] == '+':
                            res.append(left + right)
                        elif input[i] == '-':
                            res.append(left - right)
                        elif input[i] == '*':
                            res.append(left * right)
                        # # use eval
                        # res.append(eval(str(left) + input[i] + str(right)))
        return res

if __name__ == "__main__":
    input = "2-1-1"
    print(Solution().diffWaysToCompute(input))