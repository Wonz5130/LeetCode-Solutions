from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # solution one: dfs
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
    
        # solution two: loop
        if digits == "":
            return []
        d = {'2' : "abc", '3' : "def", '4' : "ghi", '5' : "jkl", '6' : "mno", '7' : "pqrs", '8' : "tuv", '9' : "wxyz"}
        ans = ['']
        for x in digits:
            ans = [y + c for c in d[x] for y in ans]
        return ans

if __name__ == "__main__":
    digits = "23"
    print(Solution().letterCombinations(digits))