from typing import List

class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        n = len(votes[0])
        # create score[26][n+1]
        score = [[0 for i in range(n+1)] for x in range(26)]
        for vote in votes:
            for i, v in enumerate(vote):
                score[ord(v) - ord("A")][i] += 1
                score[ord(v) - ord("A")][-1] = ord("Z") - ord(v) + 1  # A:26 B:25 ··· sort based on it
        score.sort(reverse=True)
        ans = ""
        for i in range(26):
            if score[i][-1] != 0:
                ans += chr(26 - score[i][-1] + 65)  # int to char
        return ans

if __name__ == "__main__":
    votes = ["ABC","ACB","ABC","ACB","ACB"]
    # votes = ["M","M","M","M"]
    print(Solution().rankTeams(votes))