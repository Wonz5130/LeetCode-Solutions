class Solution:
    def replaceSpace(self, s: str) -> str:
        # solution one
        res = ''
        for c in s:
            if c == ' ':
                res += '%20'
            else:
                res += c
        return res
        # solution two
        return ''.join(('%20' if c ==' ' else c for c in s))
        # solution three
        return s.replace(' ', '%20')