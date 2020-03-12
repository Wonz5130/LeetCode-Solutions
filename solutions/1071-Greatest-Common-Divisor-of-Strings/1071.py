class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        m, n = len(str1), len(str2)

        # solution one
        i, j = 0, 0
        while i < m or j < n:
            if str1[i % m] != str2[j % n]:
                return ""
            i += 1
            j += 1
        
        # 求最大公约数
        def gcd(a, b):
            return a if b == 0 else gcd(b, a % b)
        
        return str1[:gcd(m, n)]
        
        # solution two
        if str1 + str2 != str2 + str1:
            return ""
        
        # 求最大公约数
        def gcd(a, b):
            return a if b == 0 else gcd(b, a % b)
        
        return str1[:gcd(m, n)]

if __name__ == "__main__":
    str1 = "ABCABC"
    str2 = "ABC"
    print(Solution().gcdOfStrings(str1, str2))