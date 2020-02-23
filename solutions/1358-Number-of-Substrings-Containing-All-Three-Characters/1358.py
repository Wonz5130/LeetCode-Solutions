class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        if len(s) <= 2:
            return 0
        length = len(s)
        left, right = 0, 2
        ans = 0
        while left < length - 2:
            window = s[left: right + 1]  # [left, right + 1)
            if 'a' in window and 'b' in window and 'c' in window:
                ans += length - right  # if s[left: right + 1] satisfies, then s[left: length] also satisfies
                left += 1  # move left
            else:
                right += 1  # move right
                if right == length:  # s[left: length] does not satisfy, so s[left + x: length] also does not satisfy
                    break
        return ans

if __name__ == "__main__":
    s = "abcabc"
    print(Solution().numberOfSubstrings(s))