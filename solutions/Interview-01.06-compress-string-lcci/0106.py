class Solution:
    def compressString(self, S: str) -> str:
        n = len(S)
        res = ''
        i = 0
        while i < n:
            j = i
            while j < n and S[j] == S[i]:
                j += 1
            res += S[i] + str(j - i)
            i = j
        
        if len(res) < n:
            return res
        else:
            return S

if __name__ == "__main__":
    S = "aabcccccaaa"
    print(Solution().compressString(S))