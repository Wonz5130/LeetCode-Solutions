from typing import List

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        # solution one
        import collections
        res = 0
        cnt = collections.Counter(chars)
        for word in words:
            c = collections.Counter(word)
            if all([c[i] <= cnt[i] for i in c]):
                res += len(word)
        return res

        # solution two
        res = 0
        for word in words:
            n = len(word)
            cnt = 0
            for i in word:
                # word 中字符 i 个数 <= chars 中字符 i 个数
                if word.count(i) <= chars.count(i):
                    cnt += 1
                else:
                    break
            # word 可以由 chars 拼出
            if cnt == n:
                res += cnt
        return res

if __name__ == "__main__":
    words = ["cat","bt","hat","tree"]
    chars = "atach"
    print(Solution().countCharacters(words, chars))